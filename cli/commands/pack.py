COMMAND_NAME = 'pack'
DESCRIPTION = 'Package app into a distributable'

def run(argv):
    import argparse
    parser = argparse.ArgumentParser(prog='blanklet pack')
    parser.add_argument('--output', default='out.pack')
    args = parser.parse_args(argv)
    print(f'Packing to {args.output}')
    return 0
