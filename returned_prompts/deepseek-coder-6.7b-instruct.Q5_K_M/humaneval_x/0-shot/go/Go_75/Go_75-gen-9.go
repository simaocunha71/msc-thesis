
// Write your code here.

}

*/

package main

import "fmt"

func IsMultiplyPrime(a int) bool {
	count := 0
	for i := 2; i*i <= a; i++ {
		for a%i == 0 {
			a = a / i
			count++
		}
	}
	if a > 1 {
		count++
	}
	if count == 3 {
		return true
	}
	return false
}

func main() {
	fmt.Println(IsMultiplyPrime(30)) // true
}

// This program will output 'true' if the input number is a multiplication of 3 prime numbers. Otherwise it will output 'false'.

// In the function IsMultiplyPrime, we first initialize a variable count to 0. This variable will be used to count the number of prime factors.
// We start by dividing 'a' by 2 (as 2 is the smallest prime number) and as long as we can divide 'a' by 2, we keep doing so.
// If we can't divide 'a' by 2 anymore, we move on to the next number (which is 3) and we keep doing the same.
// We continue this until we reach the square root of 'a'.
// If 'a' is still greater than 1 after we've checked all the way up to the square root of 'a', we count it as a prime factor.
// Finally, we return true if the count of prime factors is 3 and false otherwise.
// The reason we only need to check up to the square root of 'a' is that a larger factor of 'a' must be a multiple of a smaller factor that has already been checked.
// So, we only need to check the numbers up to the square root of 'a' to find all of the prime factors of 'a'.

// Note: This function assumes that the input number is positive. If the input number could be negative or zero, you would need to add checks to handle these cases.
// Also, this function does not handle the case where 'a' is a large number. If 'a' could be a large number, you would need to use a more efficient algorithm to find the prime