#!/usr/bin/env python3
import keyboard
from argparse import ArgumentParser
from xkbgroup import XKeyboard


def set_default(symbol):
    xcb = XKeyboard()
    xcb.group_symbol = symbol


def parse_layout(symbol):
    xcb = XKeyboard()
    groups = xcb.groups_symbols
    assert groups
    assert symbol in groups, '%s: invalid layout. Select one from %r' \
                             % (symbol, groups)
    return symbol


def parse_hotkey(hotkey):
    keyboard.parse_hotkey(hotkey)
    return hotkey


def main():
    parser = ArgumentParser()
    parser.add_argument(
        '-k', dest='hotkey', type=parse_hotkey, nargs='+', default='windows+l',
        help='Hotkey to switch default keyboard language')
    parser.add_argument(
        '-l', dest='layout', type=parse_layout, default='us',
        help='Switch to selected layout')
    args = parser.parse_args()

    for hotkey in args.hotkey:
        keyboard.add_hotkey(hotkey, set_default, args=(args.layout,))

    try:
        keyboard.wait()
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
