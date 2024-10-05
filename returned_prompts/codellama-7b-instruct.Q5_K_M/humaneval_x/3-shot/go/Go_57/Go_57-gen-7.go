    if len(l) <= 1 {
        return true
    }

    if l[0] > l[1] {
        return false
    }

    for i := 1; i < len(l); i++ {
        if l[i] < l[i - 1] {
            return false
        }
    }
    return true
}



