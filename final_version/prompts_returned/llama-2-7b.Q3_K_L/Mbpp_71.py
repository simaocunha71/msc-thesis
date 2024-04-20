"""
Write a function to sort a list of elements.
assert comb_sort([5, 15, 37, 25, 79]) == [5, 15, 25, 37, 79]
"""
from typing import List

def comb_sort(arr:List[int]) -> None:
    mid = len(arr) // 2
    while True:
        if mid >= 1:
            # 交换前后两个元素，然后在中间插入合并后的元素。
            a, b = arr[0], arr[mid]
            for i in range(1, mid):
                if a > arr[i]:
                    temp = a
                    a, arr[i] = arr[i], temp
            # 在中间再进行一次交换，因为插入的位置已经变了。
            for j in range(1, mid - 1):
                if b > arr[j]:
                    temp = b
                    b, arr[j] = arr[j], temp
            
            # 循环结束后，mid = mid/2。
            mid = mid // 2
        break
"""
class Solution:
    def combSort(self, nums: List[int]) -> None:
        pass
        """
        思路：基本上是迭代思想，可以将每一个元素都加入到相应的桶中，当数组有些随机时产生了烩排序。这种方法比冒进法慢得多，但是不会导致阻塞的问题发生。
        将每一个元素都加入到相应的桶中，当数组有些随机时产生了烩排序。这种方法比冒进法慢得多，但是不会导致阻塞的问题发生
        """