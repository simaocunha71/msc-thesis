    // Check if the list is balanced
    if !IsPalindrome(q) {
        return false
    }
    // Calculate the sum of the elements
    sum := 0
    for _, v := range q {
        sum += v
    }
    // Check if the sum is less than or equal to the maximum possible weight
    return sum <= w
}

func IsPalindrome(q []int) bool {
    for i, v := range q {
        if v != q[len(q)-i-1] {
            return false
        }
    }
    return true
}