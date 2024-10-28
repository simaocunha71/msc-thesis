    if len(q) == 1{
        return q[0] <= w
    }

    if q[0] != q[len(q)-1]{
        return false
    }

    if len(q)%2 == 0{
        return q[0] + q[len(q)-1] <= w
    }

    return q[0] + q[len(q)-2] <= w
}



