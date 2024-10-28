    even_count := 0
    odd_count := 0
    for i := 1; i <= n; i++ {
        s := strconv.Itoa(i)
        if s == strconv.Itoa(int(math.Pow(10, float64(len(s))))) {
            if i % 2 == 0 {
                even_count += 1
            }else {
                odd_count += 1
            }
        }
    }
    return [2]int{even_count, odd_count}
}



