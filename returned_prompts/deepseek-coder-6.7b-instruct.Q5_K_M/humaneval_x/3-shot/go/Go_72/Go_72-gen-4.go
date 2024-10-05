    sum := 0
    for i := 0; i < len(q); i++ {
        sum += q[i]
    }
    if sum > w {
        return false
    }
    return true
}



