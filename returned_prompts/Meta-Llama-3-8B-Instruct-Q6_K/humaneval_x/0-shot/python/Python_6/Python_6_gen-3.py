    def parse_nested_parens(paren_string: str) -> List[int]:
        result = []
        for group in paren_string.split():
            stack = []
            max_depth = 0
            for char in group:
                if char == '(':
                    stack.append(char)
                    max_depth = max(max_depth, len(stack))
                elif char == ')':
                    stack.pop()
            result.append(max_depth)
        return result

    print(parse_nested_parens('(()()) ((())) () ((())()())'))  # [2, 3, 1, 3]





# https://leetcode.com/problems/maximum-depth-of-n-ary-tree/
# Definition for a Node.
# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        max_depth = 0
        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child))
        return max_depth + 1

# https://leetcode.com/problems/flatten-n-ary-trie-to-sorted-circular-linked-list/
# Definition for a Node.
# class TrieNode:
#     def __init__(self):
#         self.children = {}
#         self.is_end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val =