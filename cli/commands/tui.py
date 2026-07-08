COMMAND_NAME = 'tui'
DESCRIPTION = 'Launch the terminal UI (stub)'

def run(argv):
    import argparse
    parser = argparse.ArgumentParser(prog='blanklet tui')
    parser.add_argument('--no-colors', action='store_true')
    args = parser.parse_args(argv)
    print('Launching Blanklet TUI (stub)')
    return 0
