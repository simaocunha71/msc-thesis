    var stones = make([]int, n)

    for i:=0; i<n; i++ {
        if n%2 == 0 {
            stones[i] = n + 2*i
        } else {
            stones[i] = n + 2*i
        }
    }

    return stones
}



