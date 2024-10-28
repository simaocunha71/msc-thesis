    even := 0
    odd := 0
    for i := 1; i <= n; i++ {
        if strconv.Itoa(i) == strconv.Itoa(i)[::-1] {
            if i % 2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
}
}