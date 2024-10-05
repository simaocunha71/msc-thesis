func Monotonic(l []int) bool {
    if len(l) == 0 {
        return false
    }
    ascending := l[0] < l[len(l)-1]
    for i := 1; i < len(l); i++ {
        if ascending && l[i] < l[i-1] {
            return false
        }
        if !ascending && l[i] > l[i-1] {
            return false
        }
    }
    return true
}