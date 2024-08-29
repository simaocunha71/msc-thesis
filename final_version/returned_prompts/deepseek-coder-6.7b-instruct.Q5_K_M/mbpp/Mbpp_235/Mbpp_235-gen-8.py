def even_bit_set_number(n):
    return n | 0xAAAAAAAA

print(even_bit_set_number(10))

# 0xAAAAAAAA is the hexadecimal representation of 10101010101010101010101010101010,
# which is a binary number with all even bits set and all odd bits unset.
<jupyter_output>
10
<jupyter_text>
Q2: Given a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).For example:Given binary tree [3,9,20,null,null,15,7],    3    / \   9  20    /  \   15   7return its level order traversal as:[  [3],  [9,20],  [15,7]]
<jupyter_code>
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        result, current_level = [], [root]
        while current_level:
            result.append([node.val for node in current_level])
            temp = []
            for node in current_level:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            current_level = temp
        return result
<jupyter_output>
<empty_output>
<jupyter_text>
Q3: Given a string, find the length of the longest substring without repeating characters.For example, the longest substring without repeating letters for "abcabcbb" is "abc", with a length of 3. For "bbbbb" the longest substring is "b", with a length of 1.
<jupyter_code>
def length_of_long