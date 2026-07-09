COMMAND_NAME = 'clean'
DESCRIPTION = 'Clean build artifacts'

def run(argv):
    import argparse
    parser = argparse.ArgumentParser(prog='blanklet clean')
    parser.add_argument('--all', action='store_true')
    args = parser.parse_args(argv)
    print('Cleaning all artifacts' if args.all else 'Cleaning build artifacts')
    return 0
