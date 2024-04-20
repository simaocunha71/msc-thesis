"""
Write a function to sort the given array by using shell sort.
assert shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]) == [2, 3, 4, 5, 12, 12, 23, 56, 81, 95]
"""
import sys
from typing import List

def shell_sort(arr:List[int]):
    n = len(arr)
    for i in range (n//2 -1 , -1 , -1 ):
        j = i + n // 2
        arr[i], arr[j+1] = swap(arr, i, j)
        q = partition(arr, i)
        if not q: return
        print(f"q[{i}]: {sorted(arr[i:])}")
    for i in range (0 , n-1, 1):
        arr[i+1], arr[i] = swap(arr, i)
    #print(f"sorted({str(arr)})")
    return sorted(arr)
def swap(v: List[int], a: int, b: int)->int:
    return v.pop(a), v.append(v.pop(b))
def partition(arr: List[int], index):
    i = index +1
    j=0
    while j < arr.count(index -1):
        if i<j and arr[i]<=arr[j]:
            return True, i+1, j
        elif not (i-1 <= j and arr[i - 1] < arr[j + 1]): # 不是滑动筛选法，但是对于有序数组，会很少出现这种情况
            return True, i + 1 , j+1
        else:
            i -= 1, j += 1
    return False , i + 1,j
if __name__ == "__main__":
    sys.exit(shell_sort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95]))