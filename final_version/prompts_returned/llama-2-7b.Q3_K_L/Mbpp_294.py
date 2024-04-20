"""
Write a function to find the maximum value in a given heterogeneous list.
assert max_val(['Python', 3, 2, 4, 5, 'version'])==5
"""
class Solution(object):
    def max(self, nums):
        """
        :type nums: List[int] | [float64, int, float64, str, ...]
        :rtype: float | int
        """
        if isinstance(nums, list) and len(nums)>0:
            if type(nums[0])==list: #if it is a list of lists ,use max to get maximum value in each sublist.
                return max([max(x[1:] for x in nums)]+[nums[0][0]])#using max function on list of lists and element at index 0, to get maximum values
            elif type(nums[0])==list: #if it is a list of integers ,use max to get maximum value.
                return max([max(x)+1 for x in nums])+1#using sum function and max function on the elements to get the sum and then adding 1,the maximum integer we can have from it.
            else: #if type is int, float etc
                return max(nums) + 1##getting the element at index 0 which should be positive int value
        elif type(nums)=="str":#assuming that it is a list of strings ,using sum function on element to get the sum and then adding 1,the maximum integer we can have from each string.
            return ''.join([i + "+" for i in nums]).count("+")+1##getting the element at index 0 which should be positive int value
        else: #assuming that it is a list of lists ,using max function on element to get maximum value and then adding 1,the maximum integer we can have.
            return [max(x)+1 for x in nums] + [1]+[nums[0][0]]##getting the element at index 0 which should be positive int value
        
def main():
    print(Solution().max(['Python',3,2,'version','5']))
if __name__ == '__main__':
    main()