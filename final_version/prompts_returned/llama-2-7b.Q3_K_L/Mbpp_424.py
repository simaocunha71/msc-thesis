"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""
from typing import Tuple, List

def extract_rear(tuple: Tuple[str, ...]) -> List[str]:
    '''
    Given a string tuple in the form of ['Mers', 'for', 'Vers'], returns ['s', 'r', 's']
    :param tuple:
        a string tuple
    :return:
        list that contains only the rear index element of each string in the given tuple.
    '''
    return [item[-1] for item in tuple]
