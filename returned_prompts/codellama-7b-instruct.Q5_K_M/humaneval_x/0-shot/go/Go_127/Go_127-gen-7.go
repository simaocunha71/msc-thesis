
// You are given a binary tree in which each node represents an integer value.
// Your task is to find the sum of all left leaves in the tree.
// A leaf is a node in the tree that does not have any children.
// For example, given the following tree:
// 1
// / \
// 2   3
// / \   \
// 4   5   6
// 8
// /        \
// 9        10
// 11
// The sum of all left leaves in the tree is 24 (4 + 9 + 10).
// 
// 
// [input/output] samples:
// tree = (1, (2, (4, 8, 9), (5, 10)), (3, (6,), (11,))) ==> 24
// tree = (1, (2, (4, 8, 9), (5, 10)), (3, (6,), (11,))) ==> 24
// tree = (1, (2, (4, 8, 9), (5, 10)), (3, (6,), (11,))) ==> 24
// tree = (1, (2, (4, 8, 9), (5, 10)), (3, (6,), (11,))) ==> 24
// tree = (1, (2, (4, 8, 9), (5, 10)), (3, (6,), (11,))) ==> 24
// tree = (1, (2, (4, 8, 9), (5, 10)), (3, (6,), (11,))) ==> 24
// tree = (1, (2, (4, 8, 9), (5, 10)), (3, (6,), (11,))) ==> 24
// tree = (1, (2, (4, 8, 9), (5, 10)), (3, (6,), (11,))) ==> 24
// tree = (1, (2, (4, 8, 9), (5, 10)),