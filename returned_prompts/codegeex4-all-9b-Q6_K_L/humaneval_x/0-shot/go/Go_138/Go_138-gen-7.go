func IsEqualToSumEven(n int) bool {
    if n%2 != 0 {
        return false
    }
    if n == 4 || n == 6 {
        return false
    }
    if n > 6 {
        return true
    }
    return false
}