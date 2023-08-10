#! /usr/bin/env python

from __future__ import annotations
import sys
from graphql_pydantic_converter.schema_converter import GraphqlJsonParser
from argparse import ArgumentParser, Namespace
from typing import Optional, Sequence, Any
from enum import IntEnum
import json
from pydantic import BaseModel
from pathlib import Path

# PARSERS
arg_parser = ArgumentParser()
arg_parser.add_argument('-i', '--input-file', help='Input file path')
arg_parser.add_argument('-o', '--output-file', help='Output file path')
# arg_parser.add_argument('-V', '--version', help='show version', action='store_true')


class Exit(IntEnum):
    OK = 0
    ERROR = 1
    KeyboardInterrupt = 2


class Config(BaseModel):
    input_file: Path
    output_file: Path


def main(args: Optional[Sequence[str]] = None) -> Exit:

    if args is None:
        args = sys.argv[1:]

    namespace: Namespace = arg_parser.parse_args(args)

    # if namespace.version:
    #     my_version = __version__
    #     return Exit.OK

    try:
        config = Config(**vars(namespace))
        with open(config.input_file) as file:
            json_data: dict[str, Any] = json.load(file)
            GraphqlJsonParser(json_data).export(str(config.output_file.absolute()))
            file.close()
            return Exit.OK

    except ValueError as error:
        print(error)
        return Exit.ERROR


if __name__ == '__main__':
    sys.exit(main())
