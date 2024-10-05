
// You are given a binary tree in which each node represents a subtree
// rooted at that node. The tree may have at most 1000 nodes and at most 1000 edges.
// Each node has a key associated with it, and each non-leaf node has at most 2 children.
// For example, the tree in the diagram below is represented as the array:
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
// where each number represents a node in the tree.
// The root of the tree is node 1, and each non-leaf node's key is one more than the maximum key of its children.
// Each leaf node's key is one more than the maximum key of its parent.
// The diagram below shows the keys in the tree:
// 1
// 2   3
// 4   5   6
// 7   8   9   10
// 11  12  13  14  15
// 16
// Each node's key is unique.
// You are given a sequence of keys. Your task is to find the maximum key of the node that is the root of the subtree that contains all the given keys.
// For example, given the tree in the diagram above and the sequence:
// 4, 9, 14, 15, 2
// you should return 14 because it is the maximum key of the node that is the root of the subtree that contains the given keys.
// If no such subtree exists, return -1.
// 
// 
// [input/output] samples:
// Keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == 16
// Keys([4, 9, 14, 15, 2]) == 14
// Keys([1, 2, 3]) == -