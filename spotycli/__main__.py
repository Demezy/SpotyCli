#!/usr/bin/python3
from api import Explorer, Player

if __name__ == "__main__":
    # debug
    # input suspend program execution
    filename = Explorer.fzf_shell()
    input("delay\n")
    Player.play_media(filename)
    input("delay\n")
    Player.open_mpv(filename)
