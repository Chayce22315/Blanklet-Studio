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
    # None => use sys.argv[1:], empty list => test harness invocation with no args
    if argv is None:
        argv = sys.argv[1:]
    # If no args provided, show help
    if not argv:
        cmds = load_commands()
        print('Available commands:')
        for k in sorted(cmds):
            desc = getattr(cmds[k], 'DESCRIPTION', '')
            print(f'  {k:12} {desc}')
        return 0
    # First arg is the command; rest are passed to command module
    cmd_name = argv[0]
    cmd_args = argv[1:]
    cmds = load_commands()
    if cmd_name in ('-h','help'):
        print('Available commands:')
        for k in sorted(cmds):
            desc = getattr(cmds[k], 'DESCRIPTION', '')
            print(f'  {k:12} {desc}')
        return 0
    cmd = cmds.get(cmd_name)
    if not cmd:
        print(f'Unknown command: {cmd_name}', file=sys.stderr)
        return 2
    try:
        return cmd.run(cmd_args)
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 1
    except Exception as e:
        print(f'Error: {e}', file=sys.stderr)
        return 1

if __name__ == '__main__':
    raise SystemExit(main())
