    sum := 0
    for _, qi := range q {
        sum += qi
    }
    return sum <= w && isPalindromic(q)
}

func isPalindromic(q []int) bool {
    i, j := 0, len(q)-1
    for i < j {
        if q[i] != q[j] {
            return false
        }
        i, j = i+1, j-1
    }
    return true
}



