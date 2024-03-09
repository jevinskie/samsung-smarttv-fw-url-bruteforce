#!/usr/bin/env python3

import argparse
import locale
import logging
import sys
from typing import Final

from packaging.version import Version
from rich import print
from rich.console import Console
from rich.logging import RichHandler

from .. import _version, url_generator

locale.setlocale(locale.LC_ALL, "")

LOG_FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.WARNING,
    format=LOG_FORMAT,
    datefmt="[%X]",
    handlers=[RichHandler(console=Console(stderr=True), rich_tracebacks=True)],
)

program_name = "samsung-smarttv-fw-url-bruteforce-util"

log = logging.getLogger(program_name)


def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=program_name)
    parser.add_argument("-f", "--filename", required=True, help="filename")
    parser.add_argument("-y", "--year", type=int, required=True, help="year")
    parser.add_argument("-m", "--month", type=int, help="month")
    parser.add_argument(
        "-n",
        "--number",
        action="store_true",
        help="print the number of URLs to be checked",
    )
    parser.add_argument("-v", "--verbose", action="store_true", help="be verbose")
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s version: {Version(_version.version)}",
    )
    return parser


def real_main(args: argparse.Namespace) -> int:
    verbose: Final[bool] = args.verbose
    if verbose:
        log.setLevel(logging.INFO)
        log.info(f"{program_name}: verbose mode enabled")
    if args.number:
        print(f"{url_generator.num_url_bundles(args.month):n} URLs to check")
        return 0
    for url_bundle in url_generator.generate_url_bundles(
        args.filename, args.year, args.month
    ):
        url_bundle.url
    return 0


def main() -> int:
    try:
        args = get_arg_parser().parse_args()
        return real_main(args)
    except Exception:
        log.exception(f"Received an unexpected exception when running {program_name}")
        return 1
    except KeyboardInterrupt:
        return 0


if __name__ == "__main__":
    sys.exit(main())
