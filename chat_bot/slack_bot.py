import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
import openai

app = App(token=os.environ["SLACK_BOT_TOKEN"])
openai.api_key = os.environ["OPENAI_API_KEY"]
slack_bot_id = os.environ["SLACK_BOT_ID"]

with open("system_prompt.txt") as f:
    system_message = f.read()


@app.event("message")
def reply(event, say):
    input_message = event["text"]
    channel = event["channel"]
    user_slack_id = event["user"]

    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": input_message},
    ]
    thread_ts = event["ts"]

    # Thread case
    if "thread_ts" in event:
        thread_ts = event["thread_ts"]
        thread_messages_response = app.client.conversations_replies(
            channel=channel, ts=thread_ts
        )
        for response in thread_messages_response["messages"]:
            if response["user"] == slack_bot_id:
                messages.append(
                    {
                        "role": "assistant",
                        "content": response["text"],
                    }
                )
            elif response["user"] == user_slack_id:
                messages.append(
                    {
                        "role": "user",
                        "content": response["text"],
                    }
                )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
        )

        text = response["choices"][0]["message"]["content"]
        if text != "":
            say(text=text, thread_ts=thread_ts, channel=channel)
        else:
            print("No response from OpenAI API")
            say(text="No response from OpenAI API", thread_ts=thread_ts, channel=channel)

    except (openai.error.RateLimitError, openai.error.InvalidRequestError) as e:
        say(text="Token limit error.", thread_ts=thread_ts, channel=channel)
        print(e.user_message)


if __name__ == "__main__":
    socket_handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    socket_handler.start()
