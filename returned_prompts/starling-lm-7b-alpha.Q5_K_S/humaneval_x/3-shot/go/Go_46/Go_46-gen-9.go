    if n == 0 || n == 1 {
        return 0
    }
    if n == 2 {
        return 2
    }
    if n == 3 {
        return 0
    }
    var sequence = make([]int, 4)
    sequence[0] = 0
    sequence[1] = 0
    sequence[2] = 2
    sequence[3] = 0
    for i := 4; i <= n; i++ {
        sequence[i%4] = sequence[(i-1)%4] + sequence[(i-2)%4] + sequence[(i-3)%4] + sequence[(i-4)%4]
    }
    return sequence[n%4]
}



