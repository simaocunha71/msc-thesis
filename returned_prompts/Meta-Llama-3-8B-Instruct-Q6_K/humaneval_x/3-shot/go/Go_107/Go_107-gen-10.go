    even_count := 0
    odd_count := 0

    for i := 1; i <= n; i++ {
        str := strconv.Itoa(i)
        if str == strconv.Itoa(i)[::-1] {
            if i % 2 == 0 {
                even_count++
            } else {
                odd_count++
            }
        }
    }
    return [2]int{even_count, odd_count}
}