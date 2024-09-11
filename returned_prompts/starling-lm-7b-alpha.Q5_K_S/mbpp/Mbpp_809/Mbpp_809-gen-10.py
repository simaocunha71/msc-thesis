def check_smaller(tup1,tup2):
    for i in range(len(tup1)):
        if tup1[i] > tup2[i]:
            return False
    return True





"""
Given a string, find the longest substring that appears more than twice in the string.

If no such substring exists, return the string itself.

For example, in the string 'aaaabbbbbhaccccbabbbb', the longest substring that appears more than twice is 'bbbbha', and its length is 5.

In the string 'aaaxbbbbayayyaayayayaxayyayayayayayayaxayayayayayayyaayyaayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayay