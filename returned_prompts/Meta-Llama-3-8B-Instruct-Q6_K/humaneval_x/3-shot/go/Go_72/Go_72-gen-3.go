    if !IsBalanced(q) {
        return false
    }
    if sum := sumOf(q); sum > w {
        return false
    }
    return true
}

func IsBalanced(q []int) bool {
    for i := 0; i < len(q); i++ {
        if q[i] != q[len(q)-1-i] {
            return false
        }
    }
    return true
}

func sumOf(q []int) int {
    var sum int
    for _, v := range q {
        sum += v
    }
    return sum
}