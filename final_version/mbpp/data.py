from typing import Iterable, Dict
import gzip
import json
import os
import sys


ROOT = os.path.dirname(os.path.abspath(__file__))
MBPP = os.path.join(ROOT, sys.argv[1])

def read_problems(evalset_file: str = MBPP) -> Dict[str, Dict]:
    with open(evalset_file, 'r') as file:
        data = json.load(file)
    return data


def stream_jsonl(filename: str) -> Iterable[Dict]:
    """
    Parses each JSON entry and yields it as a dictionary
    """
    if filename.endswith(".gz"):
        with gzip.open(filename, 'rt') as fp:
            data = json.load(fp)
            for entry in data:
                yield entry
    else:
        with open(filename, "r") as fp:
            data = json.load(fp)
            for entry in data:
                yield entry


def write_jsonl(filename: str, data: Iterable[Dict], append: bool = False):
    """
    Writes an iterable of dictionaries to jsonl
    """
    if append:
        mode = 'ab'
    else:
        mode = 'wb'
    filename = os.path.expanduser(filename)
    if filename.endswith(".gz"):
        with open(filename, mode) as fp:
            with gzip.GzipFile(fileobj=fp, mode='wb') as gzfp:
                for x in data:
                    gzfp.write((json.dumps(x) + "\n").encode('utf-8'))
    else:
        with open(filename, mode) as fp:
            for x in data:
                fp.write((json.dumps(x) + "\n").encode('utf-8'))
