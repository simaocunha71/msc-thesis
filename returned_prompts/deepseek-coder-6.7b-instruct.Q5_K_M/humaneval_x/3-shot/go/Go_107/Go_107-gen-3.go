    even, odd := 0, 0
    for i := 1; i <= n; i++ {
        if isPalindrome(i) {
            if i%2 == 0 {
                even++
            } else {
                odd++
            }
        }
    }
    return [2]int{even, odd}
}

func isPalindrome(n int) bool {
    str := strconv.Itoa(n)
    for i := 0; i < len(str)/2; i++ {
        if str[i] != str[len(str)-1-i] {
            return false
        }
    }
    return true
}



