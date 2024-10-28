    left := 0
    right := len(q)-1
    sum := 0

    for left < right {
        sum += q[left] + q[right]
        left += 1
        right -= 1
    }

    return sum <= w && isPalindrome(q)
}

func isPalindrome(q []int) bool {
    left := 0
    right := len(q)-1
    for left < right {
        if q[left] != q[right] {
            return false
        }
        left += 1
        right -= 1
    }
    return true
}



