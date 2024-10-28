
    m := make(map[int]int)
    out := []int{}

    for _, num := range numbers {
        if _, ok := m[num]; !ok {
            m[num] = 1
            out = append(out, num)
        }
    }

    return out
}

func main()  {
    fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}


*/

package main

import (
	"fmt"
)

func RemoveDuplicates(numbers []int) []int {
	m := make(map[int]int)
	out := []int{}

	for _, num := range numbers {
		if _, ok := m[num]; !ok {
			m[num] = 1
			out = append(out, num)
		}
	}

	return out
}

func main() {
	fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}
/*

Problem:

You are given a 2D integer array, and your task is to rotate the array 90 degrees clockwise.

Input:

You are given a 2D integer array. The size of the array is NxN. 0 <= N <= 100.

Output:

Return the rotated array.

Example:

Input:  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Output: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

Here is a Python solution:

def rotate_matrix(matrix):
    return [list(x)[::-1] for x in zip(*matrix)]

In this solution, the `zip(*matrix)` function is used to transpose the matrix, and `[::-1]` is used to reverse each row.

Here is a Go solution:

func rotateMatrix(matrix [][]int) [][]int {
    n := len