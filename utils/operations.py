import json, glob, os, re

def do_split(obj, args):
    if obj == '':
        return []
    elif isinstance(obj, list):
        res = []
        for index, inner_obj in enumerate(obj):
            res.append(do_split(inner_obj, args))
        return res
    else:
        return obj.split(*args)

def do_strip(obj, args):
    if obj == '':
        return []
    elif isinstance(obj, list):
        res = []
        for index, inner_obj in enumerate(obj):
            res.append(do_strip(inner_obj, args))
        return res
    else:
        return obj.strip(*args)

def do_replace(obj, args):
    if obj == '':
        return []
    elif isinstance(obj, list):
        res = []
        for index, inner_obj in enumerate(obj):
            res.append(do_replace(inner_obj, args))
        return res
    else:
        return obj.replace(*args)