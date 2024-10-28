
// Insert your code here

}

*/

func IsEqualToSumEven(n int) bool {
	if n <= 2 {
		return false
	} else if n%2 != 0 {
		return false
	} else {
		return true
	}
}

func main() {
	fmt.Println(IsEqualToSumEven(4))
	fmt.Println(IsEqualToSumEven(6))
	fmt.Println(IsEqualToSumEven(8))
}

/*
	In the function `IsEqualToSumEven`, we first check if `n` is less than or equal to 2. If so, we return `false` because a number less than 2 cannot be written as the sum of exactly 4 positive even numbers.
	Then we check if `n` is odd. If so, we return `false` because an odd number cannot be written as the sum of exactly 4 positive even numbers.
	Finally, if `n` is even, we return `true` because `n` can be written as the sum of exactly 4 positive even numbers.
*/
/*
	Author: Conor O'Neill
	Date: 2023-01-10
	Program: Golang
	Purpose: Given a number n, the task is to find out whether the given number is a perfect square.
*/

package main

import (
	"fmt"
	"math"
)

/*
