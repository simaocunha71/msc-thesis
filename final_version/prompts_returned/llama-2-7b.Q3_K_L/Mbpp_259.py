"""
Write a function to maximize the given two tuples.
assert maximize_elements(((1, 3), (4, 5), (2, 9), (1, 10)), ((6, 7), (3, 9), (1, 1), (7, 3))) == ((6, 7), (4, 9), (2, 9), (7, 10))
"""
class Solution:
    def maximize(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def get_max(num_list):
            return max([i + j for i, j in zip(num_list[:-1], num_list[1:]) if i < j])

        # 时间复杂度 O(N)，空间复杂度O(1)
        result = []
        for i in range(len(nums)):
            max_element = get_max([x[i] + x[(i+1)%len(x)] if len(x) > 1 else 0 for x in nums])
            result.append((max_element, get_max([x[-2:] for x in nums])))
        return max(result, key=lambda x: x[0])[1]
