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
    var (
        // number of times each factor appeares in result
        totalTimes = make(map[int]int),
    )

    for i := 0; i < n; i++ {
        if factored, ok := totalTimes[i]; !ok {
            continue
        } else if factored > 1 {
            continue
        }
        if factor := int(math.Floor(float64(factored)) + 0.5); factor == i {
            return []int{factor}
        }
    }
    // If we get here, there is no prime divisors in the number
    panic("no prime factors found")
}
