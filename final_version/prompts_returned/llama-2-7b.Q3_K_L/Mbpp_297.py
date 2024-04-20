"""
Write a function to flatten a given nested list structure.
assert flatten_list([0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]])==[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
"""

def flatten_list(l):
    if type(l) is list:
        ans = []
        for i in l:
            if isinstance(i, list):
                a = []
                for j in i:
                    a.append(j)
                ans += a
            else:
                ans.append(i)
    return ans