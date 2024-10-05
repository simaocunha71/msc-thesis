func WillItFly(q []int,w int) bool {
    var sum int
    for _, v := range q {
        sum += v
    }
    if sum > w {
        return false
    }
    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-1-i] {
            return false
        }
    }
    return true
}