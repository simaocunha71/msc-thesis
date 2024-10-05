    even_palindrome := 0
    odd_palindrome := 0
    for i := 1; i <= n; i++ {
        number := strconv.Itoa(i)
        if number == string(reverse(number)) {
            if i % 2 == 0 {
                even_palindrome += 1
            }else {
                odd_palindrome += 1
            }
        }
    }
    return [2]int{even_palindrome, odd_palindrome}
}

func reverse(s string) string {
    r := []rune(s)
    for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}



