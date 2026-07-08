COMMAND_NAME = 'scan'
DESCRIPTION = 'Static analysis and scanning tools'

def run(argv):
    import argparse
    parser = argparse.ArgumentParser(prog='blanklet scan')
    parser.add_argument('--type', default='security')
    args = parser.parse_args(argv)
    print(f'Scanning type={args.type}')
    return 0
