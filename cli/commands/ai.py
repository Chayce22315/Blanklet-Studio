COMMAND_NAME = 'ai'
DESCRIPTION = 'Run AI assisted tasks (codegen, optimize)'

def run(argv):
    import argparse
    parser = argparse.ArgumentParser(prog='blanklet ai')
    parser.add_argument('task', nargs='?', default='help')
    args = parser.parse_args(argv)
    print(f'AI task: {args.task}')
    return 0
