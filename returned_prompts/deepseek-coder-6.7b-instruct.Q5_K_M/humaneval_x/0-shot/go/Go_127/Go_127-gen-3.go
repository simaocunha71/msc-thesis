
    // check if intervals intersect
    if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
        return "NO"
    }

    // calculate intersection
    start := max(interval1[0], interval2[0])
    end := min(interval1[1], interval2[1])
    intersection := end - start + 1

    // check if intersection length is prime
    if intersection < 2 {
        return "NO"
    }
    for i := 2; i*i <= intersection; i++ {
        if intersection%i == 0 {
            return "NO"
        }
    }

    return "YES"
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}



*/

package main

import (
	"fmt"
)

func Intersection(interval1 [2]int, interval2 [2]int) string {
	if interval1[0] > interval2[1] || interval2[0] > interval1[1] {
		return "NO"
	}
	start := max(interval1[0], interval2[0])
	end := min(interval1[1], interval2[1])
	intersection := end - start + 1
	if intersection < 2 || !isPrime(intersection) {
		return "NO"
	}
	return "YES"
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func isPrime(n int) bool {
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(Intersection([2]int{