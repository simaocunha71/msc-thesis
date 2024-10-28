
def is_palindrome(lst):
    return lst == lst[::-1]

if len(q) % 2 == 0:
    return False

if sum(q) > w:
    return False

if not is_palindrome(q):
    return False

return True

