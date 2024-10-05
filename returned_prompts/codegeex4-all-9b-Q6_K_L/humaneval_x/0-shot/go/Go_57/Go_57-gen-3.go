func Monotonic(l []int) bool {
    if len(l) < 2 {
        return true
    }
    increasing := true
    decreasing := true
    for i := 1; i < len(l); i++ {
        if l[i] > l[i-1] {
            decreasing = false
        } else if l[i] < l[i-1] {
            increasing = false
        }
        if !increasing && !decreasing {
            return false
        }
    }
    return true
}