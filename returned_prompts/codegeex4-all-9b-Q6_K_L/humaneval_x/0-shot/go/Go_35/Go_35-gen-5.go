func MaxElement(l []int) int {
    m := l[0]
    for _, v := range l {
        if v > m {
            m = v
        }
    }
    return m
}