"""
Write a function that matches a string that has an a followed by three 'b'.
assert not text_match_three("ac")
"""
from typing import Callable, Optional


def test_a():
    b = "ab"
    assert f(b) == None


def test_ba():
    b = "ba"
    assert f(b) == None


def test_bbb():
    b = "bbb"
    assert f(b) is True


def test_abb_cdee1234567890abcdefghijklmnopqrstu:
    b = "abb_cdee1234567890abcdefghijklmnopqrstu"
    assert f(b) is False


def test_a_b_c():
    b = "a_b_c"
    assert f(b) is True


def test_ab_bc1234567890abcdefghijklmnopqrstu:
    b = "ab_bc1234567890abcdefghijklmnopqrstu"
    assert f(b) is False


def test_a_b_c_d():
    b = "a_b_c_d"
    assert f(b) is True


def test_ab_abc1234567890abcdefghijklmnopqrstu:
    b = "ab_abc1234567890abcdefghijklmnopqrstu"
    assert f(b) is False


def test_a_bb_c_d():
    b = "a_bb_c_d"
    assert f(b) is True


def test_aa_bc_dd:
    b = "aa_bc_dd"
    assert f(b) is False


def test_aa_ab:
    b = "aa_ab"
    assert f(b) is False


def test_a_bbcdd:
    b = "a_abbccd"
    assert f(b) is True


def test_a_aabbcde:
    b = "a_aa