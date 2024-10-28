    even_count := 0
    odd_count := 0

    for i := 1; i <= n; i++ {
        if strconv.Itoa(i) == reverse_string(strconv.Itoa(i)){
            if i % 2 == 0 {
                even_count += 1
            }else{
                odd_count += 1
            }
        }
    }

    return [2]int{even_count, odd_count}
}

func reverse_string(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



