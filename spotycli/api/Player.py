from os import system


def play_media(filename: str):
    system("xdg-open \"" + filename + "\"")


def open_mpv(filename: str):
    system("mpv \"" + filename + '"')
