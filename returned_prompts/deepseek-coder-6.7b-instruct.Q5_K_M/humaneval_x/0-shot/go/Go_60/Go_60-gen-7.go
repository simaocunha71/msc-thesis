
// Here we create a variable "sum" to hold the sum of numbers

sum := 0

// We then create a for loop to iterate over all numbers from 1 to n

for i := 1; i <= n; i++ {

// In each iteration, we add the current number to "sum"

sum += i
}

// Finally, we return the sum

return sum
}
*/

// SumToN is a function that sums numbers from 1 to n.
func SumToN(n int) int {
	sum := 0
	for i := 1; i <= n; i++ {
		sum += i
	}
	return sum
}

// SumToN2 is a function that sums numbers from 1 to n using the formula for the sum of an arithmetic series.
func SumToN2(n int) int {
	return n * (n + 1) / 2
}

func main() {
	fmt.Println(SumToN(30))  // 465
	fmt.Println(SumToN(100)) // 5050
	fmt.Println(SumToN(5))   // 15
	fmt.Println(SumToN(10))  // 55
	fmt.Println(SumToN(1))   // 1

	fmt.Println(SumToN2(30))  // 465
	fmt.Println(SumToN2(100)) // 5050
	fmt.Println(SumToN2(5))   // 15
	fmt.Println(SumToN2(10))  // 55
	fmt.Println(SumToN2(1))   // 1
}

/*
Output:

465
5050
15
55
1
465
5050
15
55
1
*/
package main

import (
	"fmt"
	"strings"
)

// 