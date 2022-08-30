import json, glob, os, re
from utils import common, styles, operations

def config_handler(config, key):
    # Parser
    parser = config['parser']
    path = common.find_file(parser['rootDir'], parser['fileName'])
    data = None
    with open(path, encoding='utf8') as f:
        data = re.findall(parser['regex'], f.read())
    # Operator & Checker
    operators = config['operators']
    length = len(data)
    for index, arg in enumerate(data):
        data[index] = list(arg)
    for index, arg in enumerate(data):
        for operate in operators:
            target = int(operate['target'])
            args = operate['args']
            match operate['type']:
                case 'split':
                    arg[target] = operations.do_split(arg[target], args)
                case 'strip':
                    arg[target] = operations.do_strip(arg[target], args)
                case 'replace':
                    arg[target] = operations.do_replace(arg[target], args)
                case _:
                    print(styles.fatal_style("===>" + operate['type'] + " is an Invaild Operation!!!"))
                    continue
        # TODO put checker to json
        origin_str = arg[0]
        return_value = arg[1]
        function_name = arg[2]
        function_params = arg[3]
        args_str = ', '.join(function_params)
        checker = f'virtual {return_value} {function_name}({args_str}) = 0;'
        check_pass = False
        checker = checker
        if checker.replace('\n', '').replace(' ', '') == origin_str.replace('\n', '').replace(' ', ''):
            check_pass = True
        print(f'[ {index+1:3d} / {length:3d} ]', styles.check_style(check_pass), f'Checking {key}:', (return_value, function_name, function_params))
        if check_pass == False:
            print(f'    origin: {styles.fatal_style(origin_str)}')
            print(f'    parser: {styles.fatal_style(checker)}')
            return -1
    # Return
    return data

def detection(configs):
    datas = []
    for key, config in configs.items():
        print(f'===> Parsing "{key}"...')
        data = config_handler(config, key)
        if(data == -1):
            return -1
        datas.append(data)
    return datas