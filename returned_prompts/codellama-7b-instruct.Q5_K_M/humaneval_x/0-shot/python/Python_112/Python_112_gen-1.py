
def reverse_delete(s,c):
    result = ''
    for i in s:
        if i not in c:
            result += i
    if result == result[::-1]:
        return result, True
    else:
        return result, False
