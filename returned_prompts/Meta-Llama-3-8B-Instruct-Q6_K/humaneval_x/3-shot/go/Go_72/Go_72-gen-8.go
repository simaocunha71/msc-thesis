    if len(q) != len(q[:len(q)-1])+len(q[len(q)-1:]) {
        return false
    }
    sum := 0
    for _, v := range q {
        sum += v
    }
    return sum <= w
}