"""
def match_a_endb(s):
    return 'a' in s and s.endswith('b')
"""

This function uses the `in` operator to check if the string 'a' is present in the input string `s`, and the `endswith` method to check if the string ends with 'b'. The function returns `True` if both conditions are met, and `False` otherwise. The unit test `assert text_starta_endb("aabbbb")` ensures that the function works correctly.