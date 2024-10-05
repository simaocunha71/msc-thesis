    if !IsBalanced(q) {
        return false
    }
    if sum(q) > w {
        return false
    }
    return true
}

func IsBalanced(q []int) bool {
    for i, v := range q {
        if v != q[len(q)-1-i] {
            return false
        }
    }
    return true
}

func sum(q []int) int {
    total := 0
    for _, v := range q {
        total += v
    }
    return total
}