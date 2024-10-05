
// You are given a binary tree with integer values. You are also given a target value.
// Your task is to return the path from the root to the target value. The path should be
// represented as a list of values in the tree. If there is no such path, return an empty list.
// Examples:
// Search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5) == [1, 2, 5]
// Search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
// Search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11) == []
func Search(root *TreeNode, target int) []int {

B:

// You are given a non-empty array of integers.
// Your task is to return the minimum number of moves required to make all the elements of the
// array equal.
// In one move, you can increment the the value of any element by 1.
// Examples:
// MinMoves([1, 2, 3]) == 3
// MinMoves([1, 1, 1]) == 1
// MinMoves([1, 2, 3, 4, 5]) == 5
func MinMoves(arr []int) int {

C:

// You are given a string representing a binary tree. The value of each node is either "x" or "o".
// Your task is to return the maximum width of the given binary tree.
// The width of a binary tree is the maximum width among all levels of the tree.
// The binary tree is guaranteed to be valid.
// Examples:
// Width("x") == 1
// Width("o") == 1
// Width("xo") == 2
// Width("xoxoxoxoxoxoxoxoxoxoxoxoxoxoxox