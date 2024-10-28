    var count = make(map[int]int)
    for _, v := range lst {
        count[v]++
    }
    var max = -1
    for k, v := range count {
        if v >= k && k > max {
            max = k
        }
    }
    return max
}



