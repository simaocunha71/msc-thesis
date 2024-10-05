    even_num := 0
    odd_num := 0

    for i := 1; i < n; i++ {
        if is_palindrome(i) {
            if is_even(i) {
                even_num += 1
            }else{
                odd_num += 1
            }
        }
    }
    return [2]int{even_num, odd_num}
}

func is_palindrome(x int) bool {
    s := strconv.Itoa(x)
    l := len(s)
    for i := 0; i < l/2; i++ {
        if s[i] != s[l-1-i] {
            return false
        }
    }
    return true
}

func is_even(x int) bool {
    return x % 2 == 0
}




