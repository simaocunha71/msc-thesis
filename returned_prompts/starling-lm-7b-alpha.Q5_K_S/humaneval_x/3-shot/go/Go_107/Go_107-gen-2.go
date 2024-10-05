    even_count := 0
    odd_count := 0

    for i := 1; i <= n; i++ {
        str_i := strconv.Itoa(i)
        if str_i == reverse(str_i) {
            if i % 2 == 0 {
                even_count += 1
            }else {
                odd_count += 1
            }
        }
    }
    return [2]int{even_count, odd_count}
}

func reverse(s string) string {
    r := []rune(s)
    for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}




