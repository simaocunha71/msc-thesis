// The code provided returns the maximum element in the list.
// It iterates over the list, keeping track of the maximum element seen so far.
// This is a common way to find the maximum element in a list.

    var max int
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
}

// Test cases
func TestMaxElement(t *testing.T) {
    if MaxElement([]int{1, 2, 3}) != 3 {
        t.Errorf("MaxElement([1, 2, 3]) should return 3, but got %d", MaxElement([]int{1, 2, 3}))
    }
    if MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}) != 123 {
        t.Errorf("MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) should return 123, but got %d", MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
    }
}

// Run the test
func main() {
    testing.Main(func/gtest(t *testing.T) {
        TestMaxElement(t)
    })
}
B:

// Return maximum element in the list.
// >>> MaxElement([1, 2, 3])
// 3
// >>> MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
// 123
func MaxElement(l []int) int {
    max := l[0]
    for _, v := range l[1:] {
        if v > max {
            max = v
        }
    }
    return max
}

// Test cases
func TestMaxElement(t *testing.T) {
    if MaxElement([]int{1, 2, 3}) != 3 {
        t.Errorf("MaxElement([1, 2, 3]) should return 3, but got %d", MaxElement([]int{1, 2, 3}))
    }
    if MaxElement([]int{5, 3,