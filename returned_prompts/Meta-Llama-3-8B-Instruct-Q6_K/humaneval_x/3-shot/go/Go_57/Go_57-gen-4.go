    for i := 1; i < len(l); i++ {
        if (l[i-1] > l[i]) {
            return false
        }
    }
    return true
}

// OR

func Monotonic(l []int) bool {
    var increasing bool
    for i := 1; i < len(l); i++ {
        if l[i-1] > l[i] {
            return false
        }
        if l[i-1] < l[i] {
            if increasing {
                return false
            }
            increasing = true
        }
    }
    return true
}

// OR

func Monotonic(l []int) bool {
    increasing := true
    decreasing := false
    for i := 1; i < len(l); i++ {
        if l[i-1] > l[i] {
            decreasing = true
            increasing = false
        } else if l[i-1] < l[i] {
            decreasing = false
            increasing = true
        }
        if !increasing && !decreasing {
            return false
        }
    }
    return true
}