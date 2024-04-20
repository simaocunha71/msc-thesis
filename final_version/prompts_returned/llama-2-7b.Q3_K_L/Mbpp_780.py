"""
Write a function to find the combinations of sums with tuples in the given tuple list. 
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""
from typing import List

def find_combinations(tuples:List[tuple]): 
    """
    :param tuples: A list of tuples [(x1, x2) or (x1, x2, x3), ...]
    :return: List of combinations (a, b, ...) or None if there's no combination.
    """
    def find_sum(i):
        def sum_of_i(j):
            i_total = 0
            j_total = 0
            
            for t in tuples:
                if j < len(t[i]):
                    i_total += t[i][j]
                    j_total += 1
                else:
                    i_total += t[i][-1]
                    
            return i_total
        
        ans = sum_of_i(0) - sum_of_i(len(tuples))
        if not ans <= 0 or ans >= 9:
            return None
            
        return [sum_of_i(j) for j in range(1, len(tuple))]
                     
    ans = []
    
    def dfs():
        while (not find_sum(1).is_infinite):
            if not find_sum(2).is_infinite:
                ans.append(find_combinations([(a, b) for a in range(find_sum(1), sum_of_i(2))])) # (a, b) -> (b+1, a-1)
                
            if not find_sum(3).is_infinite:
                ans.append(find_combinations([(a, b, c) for a in range(find_sum(1), sum_of_i(3))])) # (a, b, c) -> (b+1, c-1, a-2)
                
            if not find_sum(4).is_infinite:
                ans.append(find_combinations([(a, b, c, d) for a in range(find_sum(1), sum_of_i(4))])) # (a, b, c, d) -> (b+1, c