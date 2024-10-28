
// A simple program which should return the value of x if n is
// a prime number and should return the value of y otherwise.
// 
// Examples:
// for XOrY(7, 34, 12) == 34
// for XOrY(15, 8, 5) == 5
func XOrY(n, x, y int) int {

    // Write your code here
    if isPrime(n) {
        return x
    } else {
        return y
    }
}

func isPrime(n int) bool {
    for i := 2; i < n; i++ {
        if n % i == 0 {
            return false
        }
    }
    return true
}
