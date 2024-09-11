"""
def sample_name(namelist):
    res = 0
    for name in namelist:
        if name[0].isupper():
            res += len(name)
    return res

def test_sample_name():
    assert sample_name(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16

test_sample_name()
"""


def sample_name(namelist):
    res = 0
    for name in namelist:
        if name[0].isupper():
            res += len(name)
    return res


def test_sample_name():
    assert sample_name(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16

test_sample_name()


def test_sample_name_1():
    assert sample_name(['bob', 'chris', 'david', 'eric']) == 11

test_sample_name_1()


def test_sample_name_2():
    assert sample_name(['alex', 'bob', 'cameron', 'david', 'eric']) == 22

test_sample_name_2()


def test_sample_name_3():
    assert sample_name(['alexandra', 'bella', 'catherine', 'diana', 'elizabeth']) == 32

test_sample_name_3()


def test_sample_name_4():
    assert sample_name(['alexandra', 'bella', 'catherine', 'diana', 'elizabeth', 'francesca']) == 40

test_sample_name_4()


def test_sample_name_5():
    assert sample_name(['alexandra', 'bella', 'catherine', 'diana', 'elizabeth', 'francesca', 'grace']) == 43

test_sample_name_5()


def test_sample_name_6():
    assert sample_name(['alexandra', 'bella', 'catherine', 'diana',