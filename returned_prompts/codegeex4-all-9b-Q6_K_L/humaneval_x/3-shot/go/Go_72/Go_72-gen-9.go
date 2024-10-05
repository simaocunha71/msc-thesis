    sum := 0
    for _, i := range q{
        sum += i
    }
    if sum > w {
        return false
    }
    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-i-1] {
            return false
        }
    }
    return true
}

