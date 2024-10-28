    if !IsBalanced(q) {
        return false
    }
    return sum(q) <= w
}

func IsBalanced(q []int) bool {
    for i := 0; i < len(q); i++ {
        if q[i] != q[len(q)-1-i] {
            return false
        }
    }
    return true
}

func sum(q []int) int {
    sum := 0
    for _, v := range q {
        sum += v
    }
    return sum
}