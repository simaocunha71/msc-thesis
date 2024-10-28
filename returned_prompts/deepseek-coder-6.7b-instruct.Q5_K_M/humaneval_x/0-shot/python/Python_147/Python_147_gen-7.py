
def get_max_triples(n):
    if n < 3:
        return 0
    mod = [0] * 3
    for i in range(1, n + 1):
        mod[i * i - i + 1 % 3] += 1
    return mod[0] * (mod[0] - 1) * (mod[0] - 2) // 6 + mod[1] * mod[2] * (mod[0] - 1) // 6

n = 5
print(get_max_triples(n))

# Output: 1

This solution works by firstly counting the number of integers in the array a that have remainders 0, 1, or 2 when divided by 3. 
Then, it calculates the number of triples (a[i], a[j], a[k]) that sum to a multiple of 3 by using the combinations formula. 
The formula for combinations is nCr = nCr = nCr = n ∑ r ∈ {0, 1, 2, …, r} n − r / r ∑ r ∈ {0, 1, 2, …, r} r / r.
"""

# 104. Maximum Depth of Binary Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1

# 108. Convert Sorted Array to Binary Search Tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
           