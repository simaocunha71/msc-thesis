def text_lowercase_underscore(input_str):
    str_list = input_str.split("_")
    for elem in str_list:
        if not(elem.isalpha() and elem.islower()):
            return False
    return True

def test_function():
    assert text_lowercase_underscore("aab_cbbbc")==(True)
    assert text_lowercase_underscore("ABC_ABC_ABC")==(False)
    assert text_lowercase_underscore("aab_cbbb_cbbc")==(True)
    assert text_lowercase_underscore("abcd_efgh_ijk")==(True)
    assert text_lowercase_underscore("a_bc")==(True)
    assert text_lowercase_underscore("abcd")==(False)
    assert text_lowercase_underscore("_abc")==(False)
    assert text_lowercase_underscore("")==(False)

test_function()























"""
def text_lowercase_underscore(input_str):
    if "_" not in input_str:
        return False
    else:
        str_list = input_str.split("_")
        for elem in str_list:
            if not(elem.isalpha() and elem.islower()):
                return False
        return True

def test_function():
    assert text_lowercase_underscore("aab_cbbbc")==(True)
    assert text_lowercase_underscore("ABC_ABC_ABC")==(False)
    assert text_lowercase_underscore("aab_cbbb_cbbc")==(True)
    assert text_lowercase_underscore("a_bc")==(True)
    assert text_lowercase_underscore("abcd")==(False)
    assert text_lowercase_underscore("_abc")==(False)
    assert text_lowercase_underscore("")==(