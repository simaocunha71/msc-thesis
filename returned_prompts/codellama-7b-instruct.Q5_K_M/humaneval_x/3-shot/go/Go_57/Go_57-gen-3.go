    if len(l) == 1 {
        return true
    }

    is_inc := l[1] > l[0]
    for i := 1; i < len(l); i++ {
        if (is_inc && l[i] < l[i-1]) || (!is_inc && l[i] > l[i-1]) {
            return false
        }
    }
    return true
}



