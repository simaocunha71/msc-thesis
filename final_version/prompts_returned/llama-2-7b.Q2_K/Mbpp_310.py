"""
Write a function to convert a given string to a tuple of characters.
assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
"""
class Solution:
    def myAtoi(self, s):
        """
        :param s: String that needs converting to a tuple of characters.
                  E.g. ('a','b','c').
        :return: A tuple of characters from the given string.
        """
        res = []
        n = len(s)
        sign = ''
        digit1, digit2, digit3, digit4, digit5, digit6 = [0] * 7
        for i in range(n):
            if s[i] == ',':
                res.append('-')
                continue
            elif s[i] == '.':
                if sign == '-':
                    res.append('.')
                else:
                    res.append('-.')
                continue
            elif s[i] == 'e' or s[i] == 'E':
                digit1 = 0 if s[:i - 1].isdigit() else int(s[:i - 1])
                sign = s[i+1:][::-1] + ''
            elif s[i] in "123456789":
                digit1 += ord('0') if len(s) <= i and (s[:i - 1]).isdigit() else int(s[:i - 1])
            elif s[i] not in 'abcdef':
                return "Invalid"
            else:
                if sign != '-' and digit1 == 0:
                    res.append((sign,digit1))
                    continue
            digit2 = ord('0') if len(s) <= i+2 and (s[i+1:][::-1]).isdigit() else int(s[i+1:])
            sign += s[i+2:][::-1] + ''
            digit3 = ord('0') * (ord('9') - ord('a') + 1) if len(s) <= i+4 and (s[:i+4]).isdigit() else int(s[:i+4])
            digit4 = ord('0') * (ord('z') - ord('a')) if len(s) <= i+5 and (s[i+4:][::-1]).