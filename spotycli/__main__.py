#!/usr/bin/python3
from api import Explorer, Player

if __name__ == "__main__":
    # debug
    # input suspend program execution
    Explorer.chdir("1media/")
    filename = Explorer.fzf_single()
    print(filename[:-1])
    input("delay\n")
    Player.open_vlc(filename)
    input("delay\n")
    Player.open_mpv(filename)
