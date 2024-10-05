// Here is the solution
func IsMultiplyPrime(a int) bool {
    // Create a boolean array "prime" of size 100, all set to true
    // Initialize the array, assuming all numbers are prime
    prime := make([]bool, 100)
    for i := 2; i < 100; i++ {
        prime[i] = true
    }
    // 0 and 1 are not prime numbers
    prime[0] = false
    prime[1] = false
    // 2 is the only even prime number
    prime[2] = true
    // Mark the multiples of each prime number starting from 2
    for i := 2; i < 100; i++ {
        if prime[i] {
            for j := i * i; j < 100; j += i {
                prime[j] = false
            }
        }
    }
    // Convert the number to its prime factors
    var factors []int
    for i := 2; i < a; i++ {
        if prime[i] && a%i == 0 {
            factors = append(factors, i)
            a /= i
        }
    }
    // Check if the number of factors is 3
    return len(factors) == 3
}