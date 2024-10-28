
if interval1[0] > interval2[0] {
	tmp := interval1
	interval1 = interval2
	interval2 = tmp
}

if interval2[0] > interval1[1] {
	return "NO"
}

if interval2[0] < interval1[0] && interval2[1] < interval1[1] {
	return "NO"
}

if interval2[0] >= interval1[0] && interval2[1] <= interval1[1] {
	return "YES"
}

if interval2[0] <= interval1[0] && interval2[1] >= interval1[1] {
	return "YES"
}

if interval2[0] >= interval1[0] && interval2[1] >= interval1[1] {
	return "YES"
}

if interval2[1] < interval1[0] {
	return "YES"
}

return "NO"
}

*/


package main

import (
	"fmt"
	"math"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	if n < 4 {
		return true
	}
	if n%3 == 0 {
		return false
	}
	if n < 9 {
		return true
	}
	if n%5 == 0 {
		return false
	}
	sqrtN := int(math.Sqrt(float64(n)))
	if sqrtN%2 == 0 && sqrtN > 2 {
		return false
	}
	for i := 7; i <= sqrtN; i += 6 {
		if i > n/i {
			break
		}
		if n%i == 0 {
			return false
		}
		if i == 2 {
			continue
		}
	