
    sum := 0

    for _, operation := range operations {
        sum += operation
        if sum < 0 {
            return true
        }
    }

    return false
}

*/

func TestBelowZero(t *testing.T) {
	testCases := []struct {
		name     string
		input    []int
		expected bool
	}{
		{"Test case 1", []int{1, 2, 3}, false},
		{"Test case 2", []int{1, 2, -4, 5}, true},
		{"Test case 3", []int{100, -50, -75, -50}, true},
		{"Test case 4", []int{100, 50, 75, 50}, false},
		{"Test case 5", []int{0, 0, 0, 0}, false},
	}

	for _, tc := range testCases {
		t.Run(tc.name, func(t *testing.T) {
			res := BelowZero(tc.input)
			if res != tc.expected {
				t.Errorf("Expected %v, got %v", tc.expected, res)
			}
		})
	}
}

func BenchmarkBelowZero(b *testing.B) {
	for i := 0; i < b.N; i++ {
		BelowZero([]int{1, 2, -4, 5})
	}
}

/*
func BelowZero(operations []int) bool {
	sum := 0

	for _, operation := range operations {
		sum += operation
		if sum < 0 {
			return true
		}
	}

	return false
}
*/
package main

import (
	"fmt"
	"strings"
)

// In this challenge, you have to establish if a string has all unique characters.
// You are not allowed to use any additional data structures (like maps or sets) to solve this problem.
// The time complexity of your solution should be O(n), and you are