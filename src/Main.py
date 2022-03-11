#!/usr/bin/python3
import Player
import Explorer

if __name__ == "__main__":
    # debug
    # input suspend program execution
    filename = Explorer.fzf_shell()
    input()
    Player.play_media(filename)
    input()
    Player.open_mpv(filename)
    
    
