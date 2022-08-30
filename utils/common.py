import json, glob, os, re

def find_file(root_dir, file_name):
    match_path = root_dir + '/**/' + file_name
    match_path = os.path.expanduser(match_path)
    for path in glob.iglob(match_path, recursive=True):
        if 'build' not in path:
            return path