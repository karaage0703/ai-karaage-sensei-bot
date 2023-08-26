# ai-karaage-sensei-bot

## Setup

```sh
$ cd && git clone https://github.com/karaage0703/ai-karaage-sensei-bot
$ cd ~/ai-karaage-sensei-bot/weblab_bot
$ docker build -t ubuntu:ai-karaage-sensei-weblab-bot .
```

## Usage

Use GPU

```sh
$ cd ~/ai-karaage-sensei-bot/weblab_bot
$ docker run -it -v $(pwd):/root --gpus all ubuntu:ai-karaage-sensei-weblab-bot
```

Use CPU

```sh
$ cd ~/ai-karaage-sensei-bot/weblab_bot
$ docker run -it -v $(pwd):/root ubuntu:ai-karaage-sensei-weblab-bot
```

In container

```sh
# make index
root@hostname:~# python3 make_index.py
```


```sh
# run bot
root@hostname:~# python3 qa_bot.py
```

```sh
# run bot with discord
root@hostname:~# python3 discord_bot.py
```


## References

- https://zenn.dev/karaage0703/articles/4097ef3ac8f51b
