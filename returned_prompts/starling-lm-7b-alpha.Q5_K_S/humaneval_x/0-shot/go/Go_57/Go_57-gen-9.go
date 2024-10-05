
    // Check if list is empty
    if len(l) == 0 {
        return true
    }

    // Check if list has only one element
    if len(l) == 1 {
        return true
    }

    // Check if list is Monotonically increasing
    for i := 0; i < len(l)-1; i++ {
        if l[i] > l[i+1] {
            return false
        }
    }

    // Check if list is Monotonically decreasing
    for i := 0; i < len(l)-1; i++ {
        if l[i] < l[i+1] {
            return false
        }
    }

    return true
}

*/

import (
    "fmt"
    "testing"
)

func TestMonotonic(t *testing.T) {
    tests := []struct {
        list []int
        want bool
    }{
        { Monotonic([]int{}), true },
        { Monotonic([]int{1}), true },
        { Monotonic([]int{1, 2}), true },
        { Monotonic([]int{1, 2, 4, 20}), true },
        { Monotonic([]int{1, 20, 4, 10}), false },
        { Monotonic([]int{4, 1, 0, -10}), true },
        { Monotonic([]int{4, 1, 0, 1}), false },
        { Monotonic([]int{4, 1, 0, 100}), false },
        { Monotonic([]int{4, 1, 100, 0}), false },
    }

    for _, test := range tests {
        got := Monotonic(test.list)
        if got != test.want {
            t.Errorf("Monotonic(%v) = %v, want %v", test.list, got, test.want)
        }
    }
}

func BenchmarkMonotonic(b *testing.B) {
    list := make([]int, 10000