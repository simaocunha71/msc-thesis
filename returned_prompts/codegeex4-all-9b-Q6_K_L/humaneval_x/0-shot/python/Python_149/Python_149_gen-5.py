def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """

    def remove_odd_length_words(lst):
        return [word for word in lst if len(word) % 2 == 0]

    def sort_by_length_and_alphabetically(lst):
        return sorted(lst, key=lambda word: (len(word), word))

    return sort_by_length_and_alphabetically(remove_odd_length_words(lst))

print(sorted_list_sum(["aa", "a", "aaa"]))  # ["aa"]
print(sorted_list_sum(["ab", "a", "aaa", "cd"]))  # ["ab", "cd"]
print(sorted_list_sum(["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]))  # ["abc", "def", "ghi", "jkl", "mno", "pqr", "stu", "vwx", "yz"]
print(sorted_list_sum(["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj", "kkk", "lll", "mmm", "nnn", "ooo", "ppp", "qqq", "rrr", "sss", "ttt", "uuu", "vvv", "www", "xxx", "yyy", "zzz"]))  # ["aaa", "bbb", "ccc", "ddd", "eee", "fff", "ggg", "hhh", "iii", "jjj", "kkk", "lll", "mmm", "nnn", "ooo", "ppp", "qqq