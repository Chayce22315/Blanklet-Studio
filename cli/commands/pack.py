COMMAND_NAME = 'pack'
DESCRIPTION = 'Package app into a distributable'

def run(argv):
    import argparse, os
    parser = argparse.ArgumentParser(prog='blanklet pack')
    parser.add_argument('--output', default='out.pack')
    args = parser.parse_args(argv)
    # create a small placeholder package file
    out = args.output
    with open(out, 'wb') as f:
        f.write(b'BLANKLET_PACK_v1\n')
        f.write(b'placeholder')
    print(f'Packing complete: {out}')
    return 0
