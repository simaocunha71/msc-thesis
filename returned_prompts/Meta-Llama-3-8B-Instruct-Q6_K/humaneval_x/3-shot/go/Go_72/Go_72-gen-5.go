    if len(q)%2==1 {
        return false
    }
    sum := 0
    for _,v := range q {
        sum += v
    }
    return sum <= w
}