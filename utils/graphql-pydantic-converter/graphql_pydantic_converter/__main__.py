#! /usr/bin/env python

from __future__ import annotations

import json
import sys
from argparse import ArgumentParser
from argparse import Namespace
from collections.abc import Sequence
from enum import IntEnum
from pathlib import Path
from typing import Any
from typing import Optional

import requests
from pydantic import BaseModel

import graphql_pydantic_converter.graphql_types
from graphql_pydantic_converter.schema_converter import GraphqlJsonParser

EXPECTED_HEADERS_PARTS = 2

# PARSERS
arg_parser = ArgumentParser()
arg_parser.add_argument('-i', '--input-file', help='Input file path')
arg_parser.add_argument('-o', '--output-file', help='Output file path')
arg_parser.add_argument('--url', help='Request json schema directly from service')
arg_parser.add_argument(
    '--headers',
    nargs='+',
    help='Add headers to request, when --url is set. --headers "HeaderName: HeaderValue" "HeaderName: HeaderValue"'
)


class Exit(IntEnum):
    OK = 0
    ERROR = 1
    KeyboardInterrupt = 2


class Config(BaseModel):
    input_file: Optional[Path]
    output_file: Optional[Path]
    url: Optional[str]
    headers: Optional[list[str]]


def parse_headers(headers):
    dict_headers = {}
    for header in headers:
        header_parts = header.split(':')
        if len(header_parts) == EXPECTED_HEADERS_PARTS:
            dict_headers[header_parts[0].strip()] = header_parts[1].strip()
    return dict_headers


def main(args: Optional[Sequence[str]] = None) -> Exit:

    if args is None:
        args = sys.argv[1:]

    namespace: Namespace = arg_parser.parse_args(args)

    print(namespace)

    try:
        config = Config(**vars(namespace))
        json_data: dict[str, Any]

        if config.url is not None:
            headers = {}

            if config.headers is not None:
                headers = parse_headers(config.headers)

            response = requests.post(
                config.url,
                data=json.dumps({'query': graphql_pydantic_converter.graphql_types.schema_request}),
                headers={'Content-Type': 'application/json'} | headers
            )
            if response.ok:
                json_data = response.json()
            else:
                raise ValueError(f'Failed to fetch JSON from URL: {config.url}')
        elif config.input_file is not None:
            with open(config.input_file) as file:
                json_data = json.load(file)
                file.close()
        else:
            raise ValueError('input-file or url must be provided')

        if config.output_file:
            GraphqlJsonParser(json_data).export(str(config.output_file.absolute()))
            return Exit.OK
        else:
            print(GraphqlJsonParser(json_data).render())
            return Exit.OK

    except Exception as error:
        print(error)
        return Exit.ERROR


if __name__ == '__main__':
    sys.exit(main())
