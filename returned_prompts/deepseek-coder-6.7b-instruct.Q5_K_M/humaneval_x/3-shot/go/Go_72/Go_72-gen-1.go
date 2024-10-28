    sum := 0
    for _, v := range q {
        sum += v
    }
    if sum > w {
        return false
    }
    return IsPalindrome(q)
}

func IsPalindrome(q  []int) bool {
    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-i-1] {
            return false
        }
    }
    return true
}



