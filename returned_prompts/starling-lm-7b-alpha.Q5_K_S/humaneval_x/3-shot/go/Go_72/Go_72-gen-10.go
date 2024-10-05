    sum := 0
    for _,qi := range q {
        sum += qi
    }

    return sum <= w && isPalindromic(q)
}

func isPalindromic(q []int) bool {
    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-1-i] {
            return false
        }
    }
    return true
}



