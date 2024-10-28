func SpecialFactorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * SpecialFactorial(n-1)
}
