
// For a given number n, find the largest number that divides n evenly, smaller than n
// >>> LargestDivisor(15)
// 5
func LargestDivisor(n int) int {
    var divisor int
    for ; n > 1; n-- {
        if n % n == 0 {
            divisor = n
            break
        }
    }
    return divisor
}
