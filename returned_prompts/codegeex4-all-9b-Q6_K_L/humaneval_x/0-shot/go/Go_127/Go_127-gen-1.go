package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5}))
}

func Intersection(interval1 [2]int, interval2 [2]int) string {
	// determine if the two intervals intersect
	start := int(math.Max(float64(interval1[0]), float64(interval2[0])))
	end := int(math.Min(float64(interval1[1]), float64(interval2[1])))

	// if there is no intersection, return "NO"
	if start > end {
		return "NO"
	}

	// calculate the length of the intersection
	length := end - start + 1

	// check if the length is a prime number
	if isPrime(length) {
		return "YES"
	} else {
		return "NO"
	}
}

func isPrime(n int) bool {
	// check if n is less than 2
	if n < 2 {
		return false
	}

	// check if n is divisible by any number up to the square root of n
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			return false
		}
	}

	// if n is not divisible by any number up to the square root of n, it is a prime number
	return true
}
