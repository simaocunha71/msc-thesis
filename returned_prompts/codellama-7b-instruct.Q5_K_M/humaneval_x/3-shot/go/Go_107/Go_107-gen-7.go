    var even_count, odd_count int
    for i := 1; i < n; i++ {
        s := strconv.Itoa(i)
        if s == reverse(s) {
            if i % 2 == 0 {
                even_count += 1
            }else{
                odd_count += 1
            }
        }
    }
    return [2]int{even_count, odd_count}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



