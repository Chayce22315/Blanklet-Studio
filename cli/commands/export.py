COMMAND_NAME = 'export'
DESCRIPTION = 'Export builds for distribution (ipa, apk, zip)'

def run(argv):
    import argparse
    parser = argparse.ArgumentParser(prog='blanklet export')
    parser.add_argument('--format', default='zip')
    args = parser.parse_args(argv)
    print(f'Exporting format={args.format}')
    return 0
