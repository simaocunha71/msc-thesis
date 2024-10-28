
func CountUpTo(n int) []int {
    result := []int{}
    if n < 2 {
        return result
    }
    for i := 2; i < n; i++ {
        if isPrime(i) {
            result = append(result, i)
        }
    }
    return result
}

func isPrime(i int) bool {
    for j := 2; j*j <= i; j++ {
        if i%j == 0 {
            return false
        }
    }
    return true
}

*/

// Implement a function that takes an non-negative integer and returns an array of the first n
// integers that are prime numbers and less than n.
// for example:
// CountUpTo(5) => [2,3]
// CountUpTo(11) => [2,3,5,7]
// CountUpTo(0) => []
// CountUpTo(20) => [2,3,5,7,11,13,17,19]
// CountUpTo(1) => []
// CountUpTo(18) => [2,3,5,7,11,13,17]
func CountUpTo(n int) []int {
    result := []int{}
    if n < 2 {
        return result
    }
    for i := 2; i < n; i++ {
        if isPrime(i) {
            result = append(result, i)
        }
    }
    return result
}

func isPrime(i int) bool {
    for j := 2; j*j <= i; j++ {
        if i%j == 0 {
            return false
        }
    }
    return true
}

*/

*/

// Implement a function that takes an non-negative integer and returns an array of the first n
// integers that are prime numbers and less than n.
// for example:
// CountUpTo(5) => [2,3]
// CountUpTo(11) => [2,3,5,7]
// CountUpTo(0)