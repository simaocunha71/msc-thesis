func WillItFly(q []int, w int) bool {
    if len(q) == 0 || w == 0 {
        return false
    }
    sum := 0
    for _, v := range q {
        sum += v
        if sum > w {
            return false
        }
    }
    for i, v := range q {
        if v != q[len(q)-1-i] {
            return false
        }
    }
    return true
}