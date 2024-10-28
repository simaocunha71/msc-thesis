
// For a given number n, find the largest number that divides n evenly, smaller than n
// >>> LargestDivisor(15)
// 5
func LargestDivisor(n int) int {
    for i := n; i > 1; i-- {
        if n % i == 0 {
            return i
        }
    }
    return 1
}
