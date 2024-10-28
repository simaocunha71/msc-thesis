    count := 0
    for _, v := range arr {
        if SumDigits(v) > 0 {
            count++
        }
    }
    return count
}

func SumDigits(n int) int {
    s := 0
    for n != 0 {
        s += n % 10
        n /= 10
    }
    return s
}

    return count
}

func SumDigits(n int) int {
    s := 0
    for n != 0 {
        s += n % 10
        n /= 10
    }
    return s
}

// IsPalindrome returns true if the number is palindrome.
func IsPalindrome(n int) bool {
    s := strconv.Itoa(n)
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        if s[i] != s[j] {
            return false
        }
    }
    return true
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

func IsOdd(n int) bool {
    return n%2 != 0
}

func isOdd(n int) bool {
    return n%2 != 0
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}

func max2(a, b, c int) int {
    if a > b {
        if a > c {
            return a
        } else {
            return c
        }
    } else {
        if b > c {
            return b
        } else {
            return c
        }
    }
}

func min(a, b int) int {