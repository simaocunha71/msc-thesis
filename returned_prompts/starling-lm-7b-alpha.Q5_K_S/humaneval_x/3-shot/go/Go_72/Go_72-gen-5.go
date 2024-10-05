    left, right := 0, len(q)-1

    for left < right {
        if q[left] != q[right] {
            return false
        }
        left++
        right--
    }
    sum := 0
    for _, value := range q {
        sum += value
    }
    return sum <= w && left == right
}



