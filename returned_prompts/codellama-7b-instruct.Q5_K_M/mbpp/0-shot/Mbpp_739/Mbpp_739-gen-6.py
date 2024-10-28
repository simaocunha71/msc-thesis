"""
def find_Index(n):
    start = 1
    end = 9
    while len(str(start)) < n:
        start = start * 10 + 1
        end = end * 10 + 9
    for i in range(start, end + 1):
        if i % 6 == 5:
            return str(i).index(str(i)[-1])
"""

