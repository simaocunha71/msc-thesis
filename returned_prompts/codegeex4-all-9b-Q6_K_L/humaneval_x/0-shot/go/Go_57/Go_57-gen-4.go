func Monotonic(l []int) bool {
    // return true if list elements are Monotonically increasing or decreasing
    return false
}

func Monotonic(l []int) bool {
    // return true if list elements are Monotonically increasing or decreasing
    if len(l) <= 1 {
        return true
    }
    increasing := false
    decreasing := false
    for i := 1; i < len(l); i++ {
        if l[i] > l[i-1] {
            increasing = true
        } else if l[i] < l[i-1] {
            decreasing = true
        }
        if increasing && decreasing {
            return false
        }
    }
    return increasing || decreasing
}