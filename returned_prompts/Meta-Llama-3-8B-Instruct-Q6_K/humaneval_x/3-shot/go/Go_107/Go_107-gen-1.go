    var even, odd int
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == strconv.Itoa(i)[::-1] {
            if i % 2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
}  // Thanks to @Santosh for the correction.



