func IsEqualToSumEven(n int) bool {
    if n < 8 {
        return false
    }
    for i := 2; i <= n; i += 2 {
        if n-i == 6 {
            return true
        }
    }
    return false
}