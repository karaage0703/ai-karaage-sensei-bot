# ai-karaage-sensei-bot(Chat Bot)

## Setup

```sh
$ cd && git clone https://github.com/karaage0703/ai-karaage-sensei-bot
$ cd ~/ai-karaage-sensei-bot/chat_bot
$ docker build -t ubuntu:ai-karaage-sensei-chat-bot .
```

- Get Open AI API KEY
- Set slack environment
- Edit `setting.sh`

## Usage

```sh
$ cd ~/ai-karaage-sensei-bot/chat_bot
$ docker run -it -v $(pwd):/root ubuntu:ai-karaage-sensei-chat-bot
```

In container

```sh
root@hostname:~# python3 source setting.sh
root@hostname:~# python3 slack-bot.py
```


## References

- https://note.com/yamayafumiteru/n/nf7aaadfa3555
- https://slack.dev/bolt-python/ja-jp/tutorial/getting-started
