
// Initialize the maximum prime factor to 2 (smallest prime number)
max_prime := 2

B:

// Divide n by 2 until n becomes odd
for n % 2 == 0 {
	n = n / 2
}

C:

// n must be odd at this point, thus skip the even numbers and iterate only for odd
for i := 3; i * i <= n; i = i + 2 {
	for n % i == 0 {
		max_prime = i
		n = n / i
	}
}

D:

// This condition is to handle the case when n is a prime number greater than 2
if n > 2 {
	max_prime = n
}

E:

return max_prime
}

// To test the code, uncomment the following lines
// fmt.Println(LargestPrimeFactor(13195)) // should print 29
// fmt.Println(LargestPrimeFactor(2048))  // should print 2

```

The logic of the function is to repeatedly divide the number n by the smallest possible divisor (which is 2) until it can no longer be divided. If the result of the division is still a composite number, the same process is repeated with the next number. The last number that was divided by without a remainder is the largest prime factor.

The time complexity of this function is O(sqrt(n)) because in the worst case scenario, the function needs to divide n by all numbers up to its square root. The space complexity is O(1) because no additional space is used that scales with the input size.

This code will be run and tested in a Go environment.

References:

1. https://en.wikipedia.org/org/wiki/Largest_prime_factor
2. https://www.geeksforgeeks.org/largest-prime-factor-number/

*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(LargestPrimeFactor(13195)) // should print 29
	fmt.Println(LargestPr