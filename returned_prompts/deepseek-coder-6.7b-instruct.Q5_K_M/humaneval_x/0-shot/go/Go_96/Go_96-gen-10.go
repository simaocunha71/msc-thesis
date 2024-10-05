
// 0 and 1 are not considered prime numbers
if n < 2 {
return []int{}
}

// Initialize a slice to hold the prime numbers
primes := make([]int, 0, n)

// Start checking from 2 up to n
for i := 2; i < n; i++ {

// Assume the number is prime until proven not to be
isPrime := true

// Check each number up to the square root of i
for j := 2; j*j <= i; j++ {
if i%j == 0 {
isPrime = false
break
}
}

// If i is prime, append it to the slice
if isPrime {
primes = append(primes, i)
}
}

// Return the slice of prime numbers
return primes
}

// Solution:
// This function works by iterating from 2 up to n and checking each number to see if it is prime. A number is considered prime if it is not divisible by any other number. The function uses a nested loop to check each number up to the square root of the number in question. If the number is divisible by any such number, it is not prime, and the function moves on to the next number. If the number is not divisible by any such number, it is prime, and the function appends it to the list of prime numbers. Finally, the function returns the list of prime numbers.
//
// The time complexity of this function is O(n*sqrt(n)), as for each number up to n, it checks up to the square root of that number. The space complexity is O(n), as it stores up to n prime numbers in the list.
//
// Note that the function could be optimized by checking only odd numbers up to the square root of n, as all even numbers (except 2) are not prime. This would reduce the number of operations by half.













































































