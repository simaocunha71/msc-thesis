// Write your code here
// If n is a prime number, return x, else return y
// You can use the Sieve of Eratosthenes algorithm to check if n is a prime number

    // Create a boolean array, prime, of size n+1
    prime := make([]bool, n+1)
    for i := 2; i <= n; i++ {
        prime[i] = true
    }

    // Use the Sieve of Eratosthenes algorithm to mark as composite (not prime) the multiples of each prime number
    for i := 2; i * i <= n; i++ {
        if prime[i] {
            for j := i * i; j <= n; j += i {
                prime[j] = false
            }
        }
    }

    // If n is prime, return x, else return y
    if prime[n] {
        return x
    } else {
        return y
    }

}

// Test the function
func main() {
    fmt.Println(XOrY(7, 34, 12)) // Should print 34
    fmt.Println(XOrY(15, 8, 5))   // Should print 5
}