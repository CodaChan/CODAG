import json, glob, os, re

def pass_style(msg):
    return f'\033[1;36;40m{msg}\033[0m'

def fatal_style(msg):
    return f'\033[1;31;40m{msg}\033[0m'

def check_style(is_pass, yes='Pass', no='Fatal'):
    if is_pass:
        return f'\033[4;36;40m{yes}\033[0m'
    else:
        return f'\033[4;31;40m{no}\033[0m'