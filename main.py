#!/usr/bin/env python3
import asyncio
import argparse
import pathlib

from lib.game import Game

DEFAULT_TIME = 60


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--time', type=int, default=DEFAULT_TIME)
    parser.add_argument('-c', '--corpus', dest='corpus_name', default='english')
    parser.add_argument('-w', '--width', type=int, default=80)
    return parser.parse_args()


def main():
    loop = asyncio.get_event_loop()
    args = parse_args()
    path = pathlib.Path(__file__).parent
    game = Game(loop, args, path)
    loop.run_until_complete(game.run())
    loop.close()


if __name__ == '__main__':
    main()
