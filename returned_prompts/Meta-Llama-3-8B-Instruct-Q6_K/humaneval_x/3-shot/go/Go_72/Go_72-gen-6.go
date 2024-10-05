    var sum int = 0
    var reverse []int = make([]int, len(q))
    copy(reverse, q)
    reverse = reverse[:len(reverse)-1]
    reverse = reverse[::-1]

    for i := 0; i < len(q); i++ {
        sum += q[i]
    }

    if len(q) != len(reverse) {
        return false
    }
    if sum > w {
        return false
    }
    return true
}