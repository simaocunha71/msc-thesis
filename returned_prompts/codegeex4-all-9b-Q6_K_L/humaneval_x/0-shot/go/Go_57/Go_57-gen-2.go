func Monotonic(l []int) bool {
    if len(l) <= 1 {
        return true
    }
    increasing := l[0] < l[1]
    for i := 1; i < len(l); i++ {
        if (l[i-1] < l[i]) != increasing {
            return false
        }
    }
    return true
}