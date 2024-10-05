    var even, odd int
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == string(s[:]) {
            if i % 2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
}