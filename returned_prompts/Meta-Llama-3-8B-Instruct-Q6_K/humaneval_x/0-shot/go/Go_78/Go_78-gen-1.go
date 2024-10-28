You can solve this problem by defining a helper function to check if a number is prime, then iterate over each character in the hexadecimal string and check if it's a prime number using the helper function. Here is the code in Go:

```go
func HexKey(num string) int {
    func isPrime(n int) bool {
        if n <= 1 {
            return false
        }
        for i := 2; i*i <= n; i++ {
            if n%i == 0 {
                return false
            }
        }
        return true
    }
    count := 0
    for _, c := range num {
        switch c {
        case '2', 'B':
            if isPrime(int(c-'0)*16 + 2) {
                count++
            }
        case '3', 'D':
            if isPrime(int(c-'0)*16 + 3) {
                count++
            }
        case '5', '7':
            if isPrime(int(c-'0)*16 + int(c-'0)) {
                count++
            }
        }
    }
    return count
}
```
This code defines a helper function `isPrime` that checks if a number is prime. Then it iterates over each character in the hexadecimal string, converts it to a decimal number, and checks if it's a prime number using the `isPrime` function. If it's a prime number, it increments the count. Finally, it returns the count.