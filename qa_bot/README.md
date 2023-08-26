# ai-karaage-sensei-bot

## Setup

```sh
$ cd && git clone https://github.com/karaage0703/ai-karaage-sensei-bot
$ cd ~/ai-karaage-sensei-bot/bot
$ docker build -t ubuntu:ai-karaage-sensei-bot .
```

## Usage

Use GPU

```sh
$ cd ~/ai-karaage-sensei-bot/bot
$ docker run -it -v $(pwd):/root --gpus all ubuntu:ai-karaage-sensei-bot
```

Use CPU

```sh
$ cd ~/ai-karaage-sensei-bot/bot
$ docker run -it -v $(pwd):/root ubuntu:ai-karaage-sensei-bot
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

- https://note.com/npaka/n/n3164e8b24539
- https://qiita.com/Kodai0417/items/3abff9575e132e2955ec
- https://qiita.com/Yumax-panda/items/9349e06f5a12d4466ca7
