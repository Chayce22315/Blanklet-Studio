COMMAND_NAME = 'build'
DESCRIPTION = 'Build the project for a target'

def run(argv):
    import argparse, time
    parser = argparse.ArgumentParser(prog='blanklet build')
    parser.add_argument('--target', default='desktop')
    parser.add_argument('--release', action='store_true')
    parser.add_argument('--clean', action='store_true')
    args = parser.parse_args(argv)
    # Simulate a build pipeline: fetch toolchain, compile, link, package
    mode = 'release' if args.release else 'debug'
    if args.clean:
        print(f'Cleaning previous build for {args.target}...')
    print(f'Starting build: target={args.target} mode={mode}')
    # pretend to run pipeline steps
    time.sleep(0.1)
    print('Toolchain: default')
    time.sleep(0.05)
    print('Compiling sources...')
    time.sleep(0.05)
    print('Linking...')
    time.sleep(0.05)
    print('Build succeeded.')
    return 0
