    increasing := true
    decreasing := true

    for i := 0; i < len(l)-1; i++ {
        if l[i] > l[i+1] {
            increasing = false
        }
        if l[i] < l[i+1] {
            decreasing = false
        }
    }

    return increasing || decreasing
}



