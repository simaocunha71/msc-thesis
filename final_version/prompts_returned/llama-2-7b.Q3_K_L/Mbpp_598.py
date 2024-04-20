"""
Write a function to check whether the given number is armstrong or not.
assert armstrong_number(153)==True
"""
from typing import Optional, List

def armstrong_number(n: Optional[int]) -> bool:
    if n is None or n == 0:
        return True

    ans = []
    count = 0
    for i in range(1, len(str(n))+1):
        sum = str(n).count(str(i)) + int(str(n).count(str(i)))
        if sum == n:
            print(str(sum), end="")
            ans.append(sum)
    for i in range(1, len(str(n))+1):
        sum = str(n).count(str(i)) * int(str(n).count(str(i)))
        if sum == n:
            print(str(sum), end="")
            ans.append(sum)
    for i in range(1, len(str(n))+1):
        sum = str(n).count(str(i)) * int(str(n).count(str(i))) * int(str(n).count(str(i)))
        if sum == n:
            print(str(sum), end="")
            ans.append(sum)
    return len(ans) == n
print(armstrong_number(153))