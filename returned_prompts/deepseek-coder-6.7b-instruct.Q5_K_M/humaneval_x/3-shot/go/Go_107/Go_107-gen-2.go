    even_count  := 0
    odd_count  := 0

    for i := 1; i <= n; i++ {
        if IsPalindrome(i) {
            if i % 2 == 0 {
                even_count++
            } else {
                odd_count++
            }
        }
    }

    return [2]int{even_count, odd_count}
}

func IsPalindrome(n int) bool {
    str := strconv.Itoa(n)
    for i := 0; i < len(str)/2; i++ {
        if str[i] != str[len(str)-i-1] {
            return false
        }
    }
    return true
}



