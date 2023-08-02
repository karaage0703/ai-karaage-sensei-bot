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


```sh
root@hostname:/# cd /root
root@hostname:~# python3 make_index.py
```


```sh
root@hostname:/# cd /root
root@hostname:~# python3 qa_bot.py
```


## References

- https://note.com/npaka/n/n3164e8b24539
