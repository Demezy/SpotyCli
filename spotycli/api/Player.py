import subprocess as sp


def open_with_default(filename: str) -> None:
    sp.run(["xdg-open", filename])


def open_mpv(filename: str) -> None:
    sp.run(["mpv", filename])


def open_vlc(filename: str) -> None:
    """open media file without user interface"""
    # TODO add controls if required
    sp.run(["cvlc", filename])
