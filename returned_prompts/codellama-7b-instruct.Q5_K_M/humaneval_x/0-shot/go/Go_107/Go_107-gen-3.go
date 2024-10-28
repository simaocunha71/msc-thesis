    for i := 1; i <= n; i++ {
        if isPalindrome(i) {
            if isEven(i) {
                // fmt.Println("even", i)
                // return [2]int{i, 0}
            } else {
                // fmt.Println("odd", i)
                // return [2]int{0, i}
            }
        }
    }
    return [2]int{0, 0}
}

func isPalindrome(n int) bool {
    s := strconv.Itoa(n)
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        if s[i] != s[j] {
            return false
        }
    }
    return true
}

func isEven(n int) bool {
    return n%2 == 0
}

