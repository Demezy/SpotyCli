import os
from subprocess import check_output

# _fzf = FzfPrompt()


def chdir(dirname: str):
    os.chdir(dirname)


def fzf_single() -> str:
    """If user cancel operation return empty string"""
    return check_output(["fzf"], universal_newlines=True).removesuffix("\n")
