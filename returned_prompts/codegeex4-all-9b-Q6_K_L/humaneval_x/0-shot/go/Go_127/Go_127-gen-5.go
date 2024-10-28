// [solution]
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

func intersectionLength(interval1 [2]int, interval2 [2]int) int {
	start := max(interval1[0], interval2[0])
	end := min(interval1[1], interval2[1])
	if start > end {
		return 0
	}
	return end - start + 1
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func Intersection(interval1 [2]int, interval2 [2]int) string {
	length := intersectionLength(interval1, interval2)
	if length == 0 {
		return "NO"
	}
	if isPrime(length) {
		return "YES"
	}
	return "NO"
}

func main() {
	fmt.Println(Intersection([2]int{1, 2}, [2]int{2, 3}))         // "NO"
	fmt.Println(Intersection([2]int{-1, 1}, [2]int{0, 4}))        // "NO"
	fmt.Println(Intersection([2]int{-3, -1}, [2]int{-5, 5}))      // "YES"
	fmt.Println(Intersection([2]int{-3, -1}, [2]int{-3, -1}))     // "YES"
	fmt.Println(Intersection([2]int{-3, 5}, [2]int{-5, 5}))       // "YES"
	fmt.Println(Intersection([2]int{1, 2}, [2]int{1, 2}))         // "YES"
	fmt.Println(Intersection([2]int{-3, 0}, [2]int{0, 3}))        // "YES"
	fmt.Println(Intersection([2]int{-3, 0}, [2]int{-3, -1}))      // "NO"
	fmt.Println(Intersection([2]int{-3, 0}, [2]int{-4, -3}))      // "NO"
	fmt.Println(Intersection([2]int{-3, 0}, [2]int{-3, 0