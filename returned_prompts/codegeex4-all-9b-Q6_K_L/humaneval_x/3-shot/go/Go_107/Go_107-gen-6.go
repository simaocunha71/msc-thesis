    count := [2]int{0,0}

    for i := 1; i <= n; i++ {
        if strconv.Itoa(i) == reverseString(strconv.Itoa(i)) {
            if i % 2 == 0 {
                count[0] += 1
            } else {
                count[1] += 1
            }
        }
    }
    return count
}

func reverseString(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}



