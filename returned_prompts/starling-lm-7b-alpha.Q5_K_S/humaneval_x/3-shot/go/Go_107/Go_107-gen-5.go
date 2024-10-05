    odd_count := 0
    even_count := 0

    for i := 1; i <= n; i++ {
        str_i := strconv.Itoa(i)
        if str_i == strconv.Itoa(reverse(strconv.ParseInt(str_i, 10, 64))) {
            if i % 2 == 0 {
                even_count += 1
            }else {
                odd_count += 1
            }
        }
    }

    return [2]int{even_count, odd_count}
}

func reverse(n int64) int64 {
    result := 0
    for n > 0 {
        result = result * 10 + (n % 10)
        n /= 10
    }
    return result
}



