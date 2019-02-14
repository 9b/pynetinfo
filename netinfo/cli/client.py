#!/usr/bin/env python
"""."""
import json
import logging
import os
import sys
from collections import OrderedDict

from argparse import ArgumentParser
from netinfo import Netinfo


CONFIG_PATH = os.path.expanduser('~/.config/backscatter')
CONFIG_FILE = os.path.join(CONFIG_PATH, 'config.json')
CONFIG_DEFAULTS = {'version': 'v0', 'api_key': ''}
URL = 'http://localhost:7777'


def main():
    """Run the core."""
    parser = ArgumentParser()
    subs = parser.add_subparsers(dest='cmd')

    setup_parser = subs.add_parser('enrich', description="Enrich addresses with data.")
    setup_parser.add_argument('-q', '--query', dest='query', required=True,
                              help='Query to search with.', type=str)
    setup_parser.add_argument('-t', '--query-type', dest='query_type', required=True,
                              help='Query type to search with.', type=str)

    args = parser.parse_args()

    if not args.cmd:
        parser.print_help()

    ni = Netinfo(URL)

    if args.cmd == 'enrich':
        response = ni.enrich(query=args.query, query_type=args.query_type)
        print(json.dumps(response, indent=4))
