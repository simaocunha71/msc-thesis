// Return maximum element in the list.
// >>> MaxElement([1, 2, 3])
// 3
// >>> MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
// 123
func MaxElement(l []int) int {
    var max int
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
}
// Time Complexity: O(n)
// Space Complexity: O(1)  // since we are using a variable, not a data structure.  // O(1)  // since we are using a variable, not a data structure.

// Test cases
func TestMaxElement(t *testing.T) {
    if MaxElement([]int{1, 2, 3}) != 3 {
        t.Errorf("MaxElement([1, 2, 3]) = %d, want 3", MaxElement([]int{1, 2, 3}))
    }
    if MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}) != 123 {
        t.Errorf("MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) = %d, want 123", MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
    }
}
// Test cases
func TestMaxElement(t *testing.T) {
    if MaxElement([]int{1, 2, 3}) != 3 {
        t.Errorf("MaxElement([1, 2, 3]) = %d, want 3", MaxElement([]int{1, 2, 3}))
    }
    if MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}) != 123 {
        t.Errorf("MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) =