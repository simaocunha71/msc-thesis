    if len(q) == 0 {
        return false
    }
    if len(q) == 1 {
        return q[0] <= w
    }
    if q[0] != q[len(q)-1] {
        return false
    }
    var sum int = 0
    for i:=0 ; i < len(q)/2 ; i++{
        sum += q[i]
        sum += q[len(q)-1-i]
    }

    if sum > w {
        return false
    }
    return true
}



