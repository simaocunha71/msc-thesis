    if len(q) == 1 {
        return q[0] <= w
    }
    sum := 0
    for _, num := range q {
        sum += num
    }
    return sum <= w && IsPalindrome(q)
}

func IsPalindrome(slice []int) bool {
    for i := range slice {
        if slice[i] != slice[len(slice)-1-i] {
            return false
        }
    }
    return true
}

