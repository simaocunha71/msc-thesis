func Monotonic(l []int) bool {
    increasing := true
    decreasing := true

    for i := 1; i < len(l); i++ {
        if l[i] < l[i-1] {
            increasing = false
        }
        if l[i] > l[i-1] {
            decreasing = false
        }
    }

    return increasing || decreasing
}