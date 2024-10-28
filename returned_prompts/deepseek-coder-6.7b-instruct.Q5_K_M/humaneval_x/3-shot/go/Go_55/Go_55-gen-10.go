    if n <= 1{
        return n
    }

    var n1, n2, res int= 0, 1, 0
    for i := 2; i <= n; i++ {
        res = n1 + n2
        n1 = n2
        n2 = res
    }
    return res
}



