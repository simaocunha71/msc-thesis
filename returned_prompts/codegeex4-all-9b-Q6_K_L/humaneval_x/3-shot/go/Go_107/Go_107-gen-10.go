    even := 0
    odd := 0

    for i := 1; i <= n; i++ {
        if strconv.Itoa(i) == reverseString(strconv.Itoa(i)) {
            if i % 2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }

    return [2]int{even, odd}
}

func reverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



