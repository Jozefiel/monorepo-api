#! /usr/bin/env python

from __future__ import annotations
import sys

import graphql_pydantic_converter.graphql_types
from graphql_pydantic_converter.schema_converter import GraphqlJsonParser
from argparse import ArgumentParser, Namespace
from typing import Optional, Sequence, Any
from enum import IntEnum
import json
from pydantic import BaseModel
from pathlib import Path
import requests

# PARSERS
arg_parser = ArgumentParser()
arg_parser.add_argument('-i', '--input-file', help='Input file path')
arg_parser.add_argument('-o', '--output-file', help='Output file path')
arg_parser.add_argument('--url', help='Request json schema directly from service')


class Exit(IntEnum):
    OK = 0
    ERROR = 1
    KeyboardInterrupt = 2


class Config(BaseModel):
    input_file: Optional[Path]
    output_file: Path
    url: Optional[str]


def main(args: Optional[Sequence[str]] = None) -> Exit:

    if args is None:
        args = sys.argv[1:]

    namespace: Namespace = arg_parser.parse_args(args)

    try:
        config = Config(**vars(namespace))
        json_data: dict[str, Any]

        if config.url is not None:
            response = requests.post(
                config.url,
                data=json.dumps({"query": graphql_pydantic_converter.graphql_types.schema_request}),
                headers={"Content-Type": "application/json"}
            )
            if response.ok:
                json_data = response.json()
            else:
                raise ValueError(f"Failed to fetch JSON from URL: {config.url}")
        elif config.input_file is not None:
            with open(config.input_file) as file:
                json_data = json.load(file)
                file.close()
        else:
            raise ValueError("input-file or url must be provided")

        try:
            GraphqlJsonParser(json_data).export(str(config.output_file.absolute()))
            return Exit.OK
        except Exception as e:
            print(e)
            return Exit.ERROR


    except ValueError as error:
        print(error)
        return Exit.ERROR


if __name__ == '__main__':
    sys.exit(main())
