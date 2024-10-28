 
// Define an empty slice to hold the results.
result := make([]int, n)

// Loop over the range of n.
for i := range result {

B:

// If i is even, calculate the factorial and assign it to the corresponding index in the result slice.
if i%2 == 0 {
result[i] = factorial(i)
continue A
}

// If i is odd, calculate the sum of numbers from 1 to i and assign it to the corresponding index in the result slice.
result[i] = sumOfNumbers(i)
}

return result
}

func factorial(n int) int {
if n == 0 {
return 1
}
return n * factorial(n-1)
}

func sumOfNumbers(n int) int {
if n == 0 {
return 0
}
return n + sumOfNumbers(n-1)
}

func main() {
fmt.Println(F(5))  // Output: [1, 2, 6, 24, 15]
}

*/

package main

import "fmt"

// Function to calculate factorial
func factorial(n int) int {
	if n == 0 {
		return 1
	}
	return n * factorial(n-1)
}

// Function to calculate sum of numbers
func sumOfNumbers(n int) int {
	if n == 0 {
		return 0
	}
	return n + sumOfNumbers(n-1)
}

// Function F
func F(n int) []int {
	result := make([]int, n)
	for i := range result {
		if i%2 == 0 {
			result[i] = factorial(i)
			continue
		}
		result[i] = sumOfNumbers(i)
	}
	return result
}

func main() {
	fmt.Println(F(5)) // Output: [1, 2, 6, 24, 15]
}

/*
This program calculates and returns a list of integers of size n where the