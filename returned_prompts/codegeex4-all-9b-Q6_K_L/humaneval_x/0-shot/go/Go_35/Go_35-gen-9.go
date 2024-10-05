func MaxElement(l []int) int {
    max := l[0]
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
}