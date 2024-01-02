
// Write a function that returns true if the given number is the multiplication of 3 prime numbers
// and false otherwise.
// Knowing that (a) is less then 100.
// Example:
// IsMultiplyPrime(30) == true
// 30 = 2 * 3 * 5
func IsMultiplyPrime(a int) bool {
    if a <= 100 {
        if a % (int32(math.Sqrt(float64(a))) + 2) == 0 { // prime checker
            return true
        } else {
            return false
        }
    }
}