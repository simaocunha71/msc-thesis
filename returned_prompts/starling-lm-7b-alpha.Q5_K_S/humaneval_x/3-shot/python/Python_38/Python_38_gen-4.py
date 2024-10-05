    # split string into groups of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[0] + group[1:]) if len(group) == 3 else group for group in groups]
    return "".join(groups)



def rotate_string_cyclic(s: str):
    """
    returns cyclic rotation of string.
    """
    return s[1:] + s[0]


def rotate_string(s: str, times: int):
    """
    returns string rotated times times.
    >>> rotate_string("abc", 2)
    'bc'
    >>> rotate_string("abc", 3)
    'cab'
    """
    return rotate_string_cyclic(s) * (times % len(s))


def rotate_list_cyclic(nums: List[int]):
    """
    returns cyclic rotation of list.
    """
    return nums[1:] + nums[0]


def rotate_list(nums: List[int], times: int):
    """
    returns list rotated times times.
    >>> rotate_list([1, 2, 3], 2)
    [2, 3, 1]
    >>> rotate_list([1, 2, 3], 3)
    [3, 1, 2]
    """
    return rotate_list_cyclic(nums) * (times % len(nums))




def shift_left(nums: List[int]):
    """
    returns list with each element shifted one position to the left.
    >>> shift_left([1, 2, 3])
    [2, 3, 1]
    """
    return nums[1:] + [nums[0]]


def shift_right(nums: List[int]):
   