"""
Write a function to remove consecutive duplicates of a given list.
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
"""

def remove_consecutive_duplicates(lst):
    d = {e: lst.count(e) for e in lst if lst.count(e)}

    result = []
    prev = None
    for cur in sorted(d):
        count = d[cur]
        while count > 0 and cur == prev + (count - 1) % len(lst):
            count -= 1
            if count >= prev:
                result.append(prev)
                prev += (count - prev) % len(lst)
    for i in range(len(result)):
        result[i] = result[i] + count // len(lst)
    return result
