    if len(l) <= 2 {
        return true
    }

    var increasing = false
    var decreasing = false

    for i := 0; i < len(l) - 1; i++ {
        if l[i] < l[i+1] {
            increasing = true
        } else if l[i] > l[i+1] {
            decreasing = true
        }

        if increasing && decreasing {
            return false
        }
    }

    return increasing || decreasing
}



