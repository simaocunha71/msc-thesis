    sum := 0
    for _, val := range q {
        sum += val
    }
    if sum > w {
        return false
    }
    for i, j := 0, len(q)-1; i < j; i, j = i+1, j-1 {
        q[i], q[j] = q[j], q[i]
    }
    for i := 1; i < len(q); i++ {
        left, right := q[:i], q[i:]
        if IsPalindrome(left) && IsPalindrome(right) {
            return true
        }
    }
    return false
}

func IsPalindrome(q []int) bool {
    for i, j := 0, len(q)-1; i < j; i, j = i+1, j-1 {
        if q[i] != q[j] {
            return false
        }
    }
    return true
}



