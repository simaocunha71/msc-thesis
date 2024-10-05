    even_count := 0
    odd_count := 0
    for i := 1; i <= n; i++ {
        number := strconv.Itoa(i)
        if number == string(reverse(number)) {
            if i % 2 == 0 {
                even_count += 1
            }else {
                odd_count += 1
            }
        }
    }
    return [2]int{even_count, odd_count}
}

func reverse(s string) []rune {
    result := make([]rune, len(s))
    for i, v := range s {
        result[len(s)-i-1] = v
    }
    return result
}



