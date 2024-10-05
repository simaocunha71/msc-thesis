
// Return true if list elements are Monotonically increasing or decreasing.
// >>> Monotonic([1, 2, 4, 20])
// true
// >>> Monotonic([1, 20, 4, 10])
// false
// >>> Monotonic([4, 1, 0, -10])
// true
func Monotonic(l []int) bool {
    // Check if list is empty
    if len(l) == 0 {
        return true
    }
    // Check if list has only one element
    if len(l) == 1 {
        return true
    }
    // Check if list is decreasing
    for i := 1; i < len(l); i++ {
        if l[i] < l[i-1] {
            return false
        }
    }
    // Check if list is increasing
    for i := 1; i < len(l); i++ {
        if l[i] > l[i-1] {
            return false
        }
    }
    // If all checks pass, return true
    return true
}

// Return true if list elements are Monotonically increasing or decreasing.
// >>> Monotonic([1, 2, 4, 20])
// true
// >>> Monotonic([1, 20, 4, 10])
// false
// >>> Monotonic([4, 1, 0, -10])
// true
func Monotonic(l []int) bool {
    // Check if list is empty
    if len(l) == 0 {
        return true
    }
    // Check if list has only one element
    if len(l) == 1 {
        return true
    }
    // Check if list is decreasing
    for i := 1; i < len(l); i++ {
        if l[i] < l[i-1] {
            return false
        }
    }
    // Check if list is increasing
    for i := 1; i < len(l); i++ {
        if l[i] > l[i-1] {
            return