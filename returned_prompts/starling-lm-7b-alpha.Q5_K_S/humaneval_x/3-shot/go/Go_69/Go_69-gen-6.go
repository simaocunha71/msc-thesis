    numToCount := map[int]int{}
    for _, v := range lst {
        numToCount[v]++
    }
    for k, v := range numToCount {
        if v >= k {
            return k
        }
    }
    return -1
}



