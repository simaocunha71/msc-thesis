
    return ''.join(char.lower() if char.isupper() else char.upper() for char in string)


if __name__ == "__main__":
    print(flip_case('Hello'))  # hELLO


Explanation:

    The function flip_case takes in a string. It uses the join and a generator comprehension to iterate through each character in the string. If the character is uppercase, it converts it to lowercase and vice versa. The resulting characters are then joined back together into a string.

"""


def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('hELLO') == 'Hello'
    assert flip_case('Python') == 'pYTHON'
    assert flip_case('pYTHON') == 'PYTHON'


test_flip_case()


if __name__ == "__main__":
    print("All tests passed.")

#task_1.py
from utils import flip_case


def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('hELLO') == 'Hello'
    assert flip_case('Python') == 'pYTHON'
    assert flip_case('pYTHON') == 'PYTHON'


test_flip_case()


if __name__ == "__main__":
    print("All tests passed.")

#task_2.py
from utils import flip_case


def test_flip_case():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('hELLO') == 'Hello'
    assert flip_case('Python') == 'pYTHON'
    assert flip_case('pYTHON') == 'PYTHON'


test_flip_case()


if __name__ == "__main__":
    print("All tests passed.")

#task_3.py
from utils import flip_case


def test_flip_case