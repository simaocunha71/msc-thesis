
    result = ""

    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()

    return result


print(flip_case('Hello'))  # should return 'hELLO'


def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('world') == 'WORLD'
    assert flip_case('Python') == 'pYTHON'
    assert flip_case('Is Fun') == 'iS fUN'


test_flip_case()


def test_flip_case_2():
    assert flip_case('hello') == 'HELLO'
    assert flip_case('WORLD') == 'world'
    assert flip_case('PYTHON') == 'python'
    assert flip_case('iS FUN') == 'IS fUN'


test_flip_case_2()


def test_flip_case_3():
    assert flip_case('1234567890') == '1234567890'
    assert flip_case('qwertyuiop') == 'QWERTYUIOP'
    assert flip_case('asdfghjkl;') == 'ASDFGHJKL;'


test_flip_case_3()


def test_flip_case_4():
    assert flip_case('') == ''


test_flip_case_4()

#Task_11_20_22_2/task_11_20_22_2.py
# https://www.codewars.com/kata/5839c48f0cf94640a20009d1

