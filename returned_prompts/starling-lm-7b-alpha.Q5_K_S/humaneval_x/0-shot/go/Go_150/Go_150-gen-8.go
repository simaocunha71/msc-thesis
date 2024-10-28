
func XOrY(n, x, y int) int {
    if isPrime(n) {
        return x
    }
    return y
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i < n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}

*/

*/

*/

```
func XOrY(n, x, y int) int {
    if isPrime(n) {
        return x
    }
    return y
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    for i := 2; i < n; i++ {
        if n%i == 0 {
            return false
        }
    }
    return true
}
```