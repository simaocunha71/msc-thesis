"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
from typing import Any, Dict, List, Optional, Set, Type, Union, overload

import functools
import logging
import os
import pprint

import numpy as np

import pytest

import tskit.algorithms.rotation_search as algs
from tskit import _

# TODO (b/173962408): Test is broken if input is a list, or an empty string. Test it again when we have tests for that.
def test_odd_equivalent():
    def f(string: str) -> int:
        logging.info("Testing %s", string)
        return algs._odd_equivalent(string=string)

    return pytest.app.subtest(f)


def odd_Equivalent(string: str = "", count: int = 0):
    """
    Returns the number of times ``count`` where you must rotate a binary string to get it's last rotation index as odd.

    Parameters
    ----------
    string : Binary string or integer type in range [1, max_length)
        Binary string or integer representing its length (if binary), and the length of rotation to apply on the string so that the output will contain an odd index, if possible.
    count : int in {0, 1, ...}
        Number of times you want to rotate the string until it contains an odd value at its last index.
            By default, this is ``0``. For example:
                If ``string="101"`, then ``count=3`` gives the output ``11110101`` which has an odd index in 4th rotation (``count=3``);
                And if ``string="0000100"`, then ``count=6`` gives the output ``111111111`` which still has an odd value in its last index (``count=7``);
            And so on.
    Returns
    -------
    ndig: int
        Number of times you need to rotate the input string, counting its end index.
        i.e.: for binary strings ``string="011001"``, count = 3;
                output is ``1110