    var fibs = make([]int, 5)
    fibs[0] = 0
    fibs[1] = 0
    fibs[2] = 2
    fibs[3] = 0
    for i:=4; i<=n; i++ {
        fibs[i] = fibs[i-1] + fibs[i-2] + fibs[i-3] + fibs[i-4]
    }
    return fibs[n]
}




