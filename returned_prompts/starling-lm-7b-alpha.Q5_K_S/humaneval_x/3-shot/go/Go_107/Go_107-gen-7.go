    even_count := 0
    odd_count := 0

    for i := 1; i <= n; i++ {
        if is_palindrome(i) {
            if i % 2 == 0 {
                even_count += 1
            }else {
                odd_count += 1
            }
        }
    }

    return [2]int{even_count, odd_count}
}

func is_palindrome(n int) bool {
    digits := make([]rune, 0)
    for n > 0 {
        digits = append(digits, rune(n % 10 + 48))
        n /= 10
    }

    for i, j := 0, len(digits) - 1; i < j; i, j = i + 1, j - 1 {
        if digits[i] != digits[j] {
            return false
        }
    }
    return true
}



