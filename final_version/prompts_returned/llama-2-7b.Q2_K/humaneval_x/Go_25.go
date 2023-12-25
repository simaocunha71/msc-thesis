import (
    "math"
)

// Return list of prime factors of given integer in the order from smallest to largest.
// Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
// Input number should be equal to the product of all factors
// >>> Factorize(8)
// [2, 2, 2]
// >>> Factorize(25)
// [5, 5]
// >>> Factorize(70)
// [2, 5, 7]
func Factorize(n int) []int {
    var list []int
    for i := 2; ; i *= 1 {
        if n%i != 0 {
            break
        } else {
            n /= i
        }
        list = append(list, i)
    }
    return list
}
