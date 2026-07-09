COMMAND_NAME = 'deps'
DESCRIPTION = 'List and manage project dependencies'

def run(argv):
    import argparse
    parser = argparse.ArgumentParser(prog='blanklet deps')
    parser.add_argument('--install', action='store_true')
    args = parser.parse_args(argv)
    if args.install:
        print('Installing dependencies...')
    else:
        print('Listing dependencies...')
    return 0
