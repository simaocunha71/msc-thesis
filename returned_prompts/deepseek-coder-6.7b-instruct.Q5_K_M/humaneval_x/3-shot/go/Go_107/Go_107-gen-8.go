    var even_count int = 0
    var odd_count int = 0

    for i:= 1; i <= n; i++ {
        if isPalindrome(i) {
            if i % 2 == 0 {
                even_count++
            } else {
                odd_count++
            }
        }
    }

    return [2]int {even_count, odd_count}
}

func isPalindrome(n int) bool {
    str := strconv.Itoa(n)
    for i:= 0; i < len(str)/2; i++ {
        if str[i] != str[len(str)-1-i] {
            return false
        }
    }
    return true
}


