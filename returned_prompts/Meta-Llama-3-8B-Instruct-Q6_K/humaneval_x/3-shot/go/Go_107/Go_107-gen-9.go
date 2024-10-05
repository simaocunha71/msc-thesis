    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        str := strconv.Itoa(i)
        if str == strconv.Itoa(i)[::-1] {
            if i % 2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
} 





