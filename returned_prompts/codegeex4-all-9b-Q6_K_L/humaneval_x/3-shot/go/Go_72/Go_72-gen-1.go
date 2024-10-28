    var sum int = 0
    for _, i := range q {
        sum += i
    }

    if (sum <= w) && (isPalindrome(q)) {
        return true
    }

    return false
}

func isPalindrome(q []int) bool {
    left := 0
    right := len(q) - 1

    for left < right {
        if q[left] != q[right] {
            return false
        }

        left++
        right--
    }

    return true
}

