import argparse
import logging
import sys

from kshark.debug import Debug

def argParser():
    parser = argparse.ArgumentParser(description="kubectl shark configurations")

    parser.add_argument(
        "--mode",
        action='store',
        type=str,
        choices=["stream", "analysis"],
        help="The identifier of the mode ",
        default="stream")

    parser.add_argument(
        "--pod",
        action='store',
        type=str,
        help="The identifier of the pod which should get in track",
        required=True)

    parser.add_argument(
        "--interface",
        action='store',
        type=str,
        help="The identifier of the interface which should get in track",
        default="eth0")

    parser.add_argument(
        "--namespace",
        action='store',
        type=str,
        help="The namespace identifier",
        default="default"
    )

    return parser.parse_args()

def main():
    debugObj = Debug()
    args = argParser()

    parameters = {}
    parameters["mode"] = args.mode
    parameters["pod"] = args.pod
    parameters["interface"] = args.interface
    parameters["namespace"] = args.namespace

    debugObj.getDump(parameters)
