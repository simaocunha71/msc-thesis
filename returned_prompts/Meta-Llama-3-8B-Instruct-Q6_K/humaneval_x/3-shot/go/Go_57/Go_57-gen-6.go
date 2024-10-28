    increasing := true
    decreasing := true
    for i := 1; i < len(l); i++ {
        if l[i-1] < l[i] {
            decreasing = false
        } else if l[i-1] > l[i] {
            increasing = false
        }
    }
    return increasing || decreasing
}