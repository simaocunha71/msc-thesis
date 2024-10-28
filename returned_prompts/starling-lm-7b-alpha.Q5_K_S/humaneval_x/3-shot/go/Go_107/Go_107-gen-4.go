    even_count, odd_count := 0, 0
    for i := 1; i <= n; i++ {
        str_i := strconv.Itoa(i)
        if str_i == strconv.Itoa(int(math.Mod(float64(i), 10))) {
            if i%2 == 0 {
                even_count += 1
            }else {
                odd_count += 1
            }
        }
    }
    return [2]int{even_count, odd_count}
}



