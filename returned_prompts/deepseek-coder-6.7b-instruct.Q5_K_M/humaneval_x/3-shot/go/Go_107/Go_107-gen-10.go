    evenCount := 0
    oddCount := 0
    for i := 1; i <= n; i++ {
        if isPalindrome(i) {
            if i % 2 == 0 {
                evenCount++
            } else {
                oddCount++
            }
        }
    }
    return [2]int{evenCount, oddCount}
}

func isPalindrome(n int) bool {
    str := strconv.Itoa(n)
    for i := 0; i < len(str)/2; i++ {
        if str[i] != str[len(str)-i-1] {
            return false
        }
    }
    return true
}



