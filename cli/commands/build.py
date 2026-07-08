COMMAND_NAME = 'build'
DESCRIPTION = 'Build the project for a target'

def run(argv):
    import argparse
    parser = argparse.ArgumentParser(prog='blanklet build')
    parser.add_argument('--target', default='desktop')
    parser.add_argument('--release', action='store_true')
    args = parser.parse_args(argv)
    print(f'Building target={args.target} release={args.release}')
    return 0
