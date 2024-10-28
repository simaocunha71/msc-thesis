
    // Your code here

    return 0
}

*/

package main

import (
	"fmt"
	"math"
)

func LargestPrimeFactor(n int) int {
	var maxPrime int = -1

	// Divide n by 2 until it is odd
	for n%2 == 0 {
		maxPrime = 2
		n >>= 1
	}

	// n must be odd at this point, so find odd factors of n
	for i := 3; i <= int(math.Sqrt(float64(n))); i += 2 {
		for n%i == 0 {
			maxPrime = i
			n = n / i
		}
	}

	// If n is a prime and greater than 2
	if n > 2 {
		maxPrime = n
	}

	return maxPrime
}

func main() {
	fmt.Println(LargestPrimeFactor(13195)) // Expected output: 29
	fmt.Println(LargestPrimeFactor(2048))  // Expected output: 2
}
package main

import (
	"testing"
)

func TestLargestPrimeFactor(t *testing.T) {
	type test struct {
		input    int
		expected int
	}

	tests := []test{
		{input: 13195, expected: 29},
		{input: 2048, expected: 2},
		{input: 60, expected: 5},
		{input: 17, expected: 17},
		{input: 33, expected: 11},
	}

	for _, test := range tests {
		if output := LargestPrimeFactor(test.input); output != test.expected {
			t.Errorf("LargestPrimeFactor(%d) = %d; want %d", test.input, output, test.expected)
		}
	}
}

func BenchmarkLargestPrimeFactor(b *testing.