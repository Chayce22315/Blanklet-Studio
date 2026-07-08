#!/usr/bin/env python3
"""Blanklet CLI entrypoint - discovers and runs commands in cli.commands
"""
import argparse
import importlib
import pkgutil
import sys
from pathlib import Path

def load_commands():
    cmds = {}
    package_path = Path(__file__).parent / 'commands'
    for finder, name, ispkg in pkgutil.iter_modules([str(package_path)]):
        if name.startswith('_'):
            continue
        module = importlib.import_module(f'cli.commands.{name}')
        cmd_name = getattr(module, 'COMMAND_NAME', name)
        cmds[cmd_name] = module
    return cmds

def main(argv=None):
    # treat only None as 'use sys.argv'; allow empty list to mean no args
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(prog='blanklet', description='Blanklet CLI')
    parser.add_argument('command', nargs='?', help='Command to run')
    parser.add_argument('args', nargs=argparse.REMAINDER)
    parsed = parser.parse_args(argv[:1])
    cmds = load_commands()
    if not parsed.command or parsed.command in ('-h','help'):
        print('Available commands:')
        for k in sorted(cmds):
            desc = getattr(cmds[k], 'DESCRIPTION', '')
            print(f'  {k:12} {desc}')
        return 0
    cmd = cmds.get(parsed.command)
    if not cmd:
        print(f'Unknown command: {parsed.command}', file=sys.stderr)
        return 2
    try:
        return cmd.run(parsed.args)
    except SystemExit as e:
        # allow commands to call sys.exit(code)
        return e.code if isinstance(e.code, int) else 1
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
