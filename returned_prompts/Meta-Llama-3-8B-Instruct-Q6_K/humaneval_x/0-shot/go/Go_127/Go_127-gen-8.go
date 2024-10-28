Here is the Go solution for the problem:
```go
package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func Intersection(interval1 [2]int, interval2 [2]int) string {
	min := math.MaxFloat64
	max := math.MinFloat64
	if interval1[0] < interval2[0] {
		min = float64(interval1[0])
	} else {
		min = float64(interval2[0])
	}
	if interval1[1] > interval2[1] {
		max = float64(interval1[1])
	} else {
		max = float64(interval2[1])
	}

	if max <= min {
		return "NO"
	}

	intersectionLength := int(max - min)
	if isPrime(intersectionLength) {
		return "YES"
	} else {
		return "NO"
	}
}

func main() {
	fmt.Println(Intersection([2]int{1, 2}, [2]int{2, 3})) // "NO"
	fmt.Println(Intersection([2]int{-1, 1}, [2]int{0, 4})) // "NO"
	fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5})) // "YES"
}
```
In this solution, we first find the minimum and maximum values of the intersection of the two intervals. If the maximum is less than or equal to the minimum, it means that the intervals do not intersect, so we return "NO". Otherwise, we calculate the length of the intersection and check if it is a prime number using the `isPrime` function. If it is, we return "YES", otherwise we return "NO". The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If it is not divisible, it is a prime number. The `main` function tests the `Intersection` function with different input intervals and prints the results.