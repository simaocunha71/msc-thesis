
// You are given a binary tree. Each node in the tree has a value and two children. The value of each
// node is either 0, 1, or 2. Return the number of nodes in the tree.
// Examples:
// Tree(nil) == 0
// Tree([0, [0, 0, 0], [1, 1, 1]]) == 7
// Tree([0, [0, 0, 0], [2, 1, 1]]) == 6
// Tree([0, [0, 0, 0], [2, 2, 1]]) == 5
// Tree([0, [0, 0, 0], [2, 2, 2]]) == 4
// Tree([0, [0, 0, 0], [2, 2, 2], [2, 2, 2]]) == 3
// Tree([0, [0, 0, 0], [2, 2, 2], [2, 2, 2], [2, 2, 2]]) == 2
// Tree([0, [0, 0, 0], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]]) == 1
// Tree([0, [0, 0, 0], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2], [2, 2, 2]]) == 0
func Tree(t *TreeNode) int {

B:

// You are given a positive integer n. Return the nth Fibonacci number.
// The Fibonacci sequence starts like this: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
// Examples:
// Fibonacci(0) == 0
// Fibonacci(1) == 1
// Fibonacci(2) == 1
// Fibonacci(