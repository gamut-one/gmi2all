#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__version__ = "0.0.2"

import sys
import logging
import argparse
import os.path
import textwrap
import urllib.parse


def to_html(fobj, args):
    buffer = '<html><head>\n<meta charset="UTF-8">'
    if args.stylesheet:
        if isinstance(args.stylesheet, str):
            stylesheet = [args.stylesheet]
        else:
            stylesheet = args.stylesheet
        for sheet in stylesheet:
            buffer += f'<link href="{sheet}" rel="stylesheet" type="text/css">\n'

    buffer += '</head><body>\n'
    preform = False
    for line in fobj.readlines():
        line = line
        if len(line) == 0:
            continue
        elif line.startswith('```'):
            if preform == True:
                preform = False
                buffer += '</pre>\n'
                continue
            else:
                preform = True
                buffer += '<pre>\n'
                continue
        elif line.startswith('###'):
            buffer += f'<h3>{line[3:].strip()}</h3>\n'
        elif line.startswith('##'):
            buffer += f'<h2>{line[2:].strip()}</h2>\n'
        elif line.startswith('#'):
            buffer += f'<h1>{line[1:].strip()}</h1>\n'
        elif line.startswith('=>'):
            line = line[2:].strip()
            res = line.split(' ')
            if len(res) > 1:
                name = ' '.join(res[1:])
                buffer += f'<p><a href="{res[0]}">{name}</a></p>\n'
            else:
                buffer += f'<p><a href="{res[0]}">{res[0]}</a></p>\n'
        elif line.startswith('*'):
            buffer += f'<li>{line[1:].strip()}</li>\n'
        elif line.startswith('>'):
            buffer += f'<blockquote><q>{line[1:].strip()}</q></blockquote>\n'
        else:
            if preform:
                buffer += line
            else:
                if len(line.strip()) > 0:
                    if args.fixed_width_p:
                        buffer += '<p>'
                        for fline in textwrap.wrap(line.strip(), width=args.width):
                            buffer += fline + '<br/>'
                        buffer += '</p>\n'
                    else:
                        buffer += f'<p>{line.strip()}</p>\n'
    buffer += '</body></html>\n'
    return buffer


def to_gophermap(fobj, args):
    buffer = ''
    preform = False
    for line in fobj.readlines():
        line = line
        if len(line.strip()) == 0:
            buffer += '\n'
        elif line.startswith('```'):
            if preform == True:
                preform = False
                continue
            else:
                preform = True
                continue
        elif line.startswith('###'):
            buffer += f'{line[3:].strip()}\n' + ('-' * len(line[3:].strip())) + '\n'
        elif line.startswith('##'):
            buffer += f'{line[2:].strip()}\n' + ('-' * len(line[3:].strip())) + '\n'
        elif line.startswith('#'):
            buffer += f'{line[1:].strip()}\n' + ('=' * len(line[3:].strip())) + '\n'
        elif line.startswith('=>'):
            line = line[2:].strip()
            res = line.split(' ')

            if res[0].startswith('gopher://'):
                o = urllib.parse.urlparse(res[0])
                path = o.path or '/'
                port = o.port or 70
                buffer += f'1{res[1]}\t{path}\t{o.hostname}\t{port}\n'
            else:
                if len(res) > 1:
                    name = ' '.join(res[1:])
                    buffer += f'h{name}\tURL:{res[0]}\tnull.host\t70\n'
                else:
                    buffer += f'h{res[0]}\tURL:{res[0]}\tnull.host\t70\n'
        elif line.startswith('*'):
            buffer += f'* {line[1:].strip()}\n'
        elif line.startswith('>'):
            for fline in textwrap.wrap(textwrap.indent(line, ' ' * 4), width=args.width):
                buffer += fline + '\n'
        else:
            if preform:
                buffer += line
            else:
                if len(line.strip()) > 0:
                    for fline in textwrap.wrap(line.strip(), width=args.width):
                        buffer += fline + '\n'
    return buffer


def to_plain(fobj, args):
    pass


FORMATS = {
    'html': to_html,
    'gophermap': to_gophermap,
}


def main():
    logging.basicConfig(level=logging.INFO, format='%(message)s')

    parser = argparse.ArgumentParser()
    parser.add_argument('--version', action='version', version=__version__)
    parser.add_argument('-f', '--format', help='output format')
    parser.add_argument('-o', '--output', help='output filename', default=None)
    parser.add_argument('file')

    # HTML arguments
    parser.add_argument('--stylesheet', action='append',
                        help='Name of a stylesheet to link in the header of HTML documents')
    parser.add_argument('--fixed-width-p', action='store_true',
                        help='Limit the length of lines in a paragraph by the width value')

    # Gopher / Plaintext arguments
    parser.add_argument(
        '--width', help='Column width to use for Gopher and Plain', type=int, default=70)
    args = parser.parse_args()

    input_filename = os.path.abspath(args.file)
    if not os.path.exists(input_filename):
        logging.error(f'file {input_filename} does not exist')
        return 1

    if args.format not in FORMATS:
        logging.error(f'Unknown format {args.format}')
        return 1

    with open(input_filename, encoding='utf-8') as ifobj:
        formatted = FORMATS[args.format](ifobj, args)

    if args.output:
        with open(args.output, 'w', encoding='utf-8') as ofobj:
            ofobj.write(formatted)
    else:
        sys.stdout.write(formatted)


if __name__ == '__main__':
    sys.exit(main())
