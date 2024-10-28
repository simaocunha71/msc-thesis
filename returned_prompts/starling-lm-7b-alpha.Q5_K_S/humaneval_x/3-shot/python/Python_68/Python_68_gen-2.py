    def pluck(arr):
        """
        Given an array representing a branch of a tree that has non-negative integer nodes
        your task is to pluck one of the nodes and return it.
        The plucked node should be the node with the smallest even value.
        If multiple nodes with the same smallest even value are found return the node that has smallest index.

        The plucked node should be returned in a list, [ smalest_value, its index ],
        If there are no even values or the given array is empty, return [].

        Example 1:
            Input: [4,2,3]
            Output: [2, 1]
            Explanation: 2 has the smallest even value, and 2 has the smallest index.

        Example 2:
            Input: [1,2,3]
            Output: [2, 1]
            Explanation: 2 has the smallest even value, and 2 has the smallest index. 

        Example 3:
            Input: []
            Output: []
        
        Example 4:
            Input: [5, 0, 3, 0, 4, 2]
            Output: [0, 1]
            Explanation: 0 is the smallest value, but  there are two zeros,
                         so we will choose the first zero, which has the smallest index.

        Constraints:
            * 1 <= nodes.length <= 10000
            * 0 <= node.value
        """

        result = []
        for idx, elem in enumerate(arr):
            if elem % 2 == 0:
                result.append([elem, idx])

        if len(result) == 0:
            return []

        return result[0]


# [3, 6, 8, 9, 2]

def find_min_in_rotated_sorted_array(nums: List[int]) -> int:
    """
    There is an integer array nums sorted in ascending order; however, it is rotated at some pivot unknown to you
    beforehand. (i.e., the same element appears multiple times).
