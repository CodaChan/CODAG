# /
# Code Online Detection and Generation, CODAG
# Author: codachans@gmail.com, CodaChan
# Date: 2022-8-18 
# /

import json, glob, os, re
from utils import common, styles, operations

from detection import detection
from generation import generation

def run():
    with open('configs.json') as config_file:
        configs = json.load(config_file)   
        datas = detection(configs['detectionConfigs'])
        if datas == -1:
            return -1
        result = generation(configs['generationConfigs'], datas)
        if result == -1:
            return -1
        return 0

if __name__ == '__main__':
    run()