    var even_count int = 0
    var odd_count int = 0

    for i := 1; i <= n; i++ {
        if IsPalindrome(strconv.Itoa(i)) && i % 2 == 0 {
            even_count += 1
        }else if IsPalindrome(strconv.Itoa(i)) && i % 2 == 1{
            odd_count += 1
        }
    }
    return [2]int{even_count, odd_count}
}
func IsPalindrome(s string) bool {
    for i := 0; i < len(s); i++ {
        if s[i] != s[len(s)-1-i] {
            return false
        }
    }
    return true
}

