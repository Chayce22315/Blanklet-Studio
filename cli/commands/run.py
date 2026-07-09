COMMAND_NAME = 'run'
DESCRIPTION = 'Run the project locally'

def run(argv):
    import argparse
    parser = argparse.ArgumentParser(prog='blanklet run')
    parser.add_argument('--target', default='desktop')
    args = parser.parse_args(argv)
    print(f'Running target={args.target}')
    return 0
