"""
Write a function to find the Eulerian number a(n, m).
assert eulerian_num(3, 1) == 4
"""
class Solution:
    def eulerian_number(self, n: int, m: int) -> int:
        '''
            时间复杂度：O(m^2.n^2)；空间复杂度：O(1).
            因为每次求一个数，都需要遍历所有的数组中，那么空间复杂度是固定的。
        
        '''
        if n == 0 or m == 0:
            return -1

        # 先找到一个包罗架乎每个数字，如果没有就不加上
        def is_eulerian(num, num_list):
            if len(num_list) == n:
                return True
            else:
                for i in range(0, n - 1):
                    if (num[i] + num[i+1]) % 2 != num[i]:
                        return False
                return True
        
        result = []
        def helper(i, j) -> int:
            cur_result = 0
            
            for k in range(0, i-1):
                if (cur_num[k] + sum(nums[:j]) == nums[k+1][j+1] and is_eulerian(nums[k+1][j+1], num_list)):
                    cur_result = helper(i-1, j) + 1
                else:
                    return -1
            if (cur_num[i-1] + sum(nums[:j]) == nums[i-1][j+1] and is_eulerian(nums[i-1][j+1], num_list)): 
                cur_result = helper(i, j) + 1
            if (cur_num[0] + sum(nums[:]) == nums[0][1] and is_eulerian(nums[0][1], num_list)):
                cur_result += 1
            
            for k in range(i, j):
                if (cur_num[k-1]