import os
from pyfzf import FzfPrompt
from subprocess import CalledProcessError, check_output

# _fzf = FzfPrompt()


def chdir(dirname: str):
    os.chdir(dirname)


def fzf_shell() -> str:
    """If user cancel operation return empty string"""
    try:
        return str(check_output("fzf", shell=True))[2:-3]
    except CalledProcessError:
        return ""
