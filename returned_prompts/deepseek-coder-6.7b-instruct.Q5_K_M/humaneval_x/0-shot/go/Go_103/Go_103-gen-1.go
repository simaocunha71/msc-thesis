  if n > m {
    return -1
  }

B:
  avg := math.Round(float64(n+m) / 2)

C:
  return fmt.Sprintf("%b", int(avg))

}

Answer:
The function RoundedAvg(n, m int) interface{} is computing the average of the integers from n through m. It checks if n is greater than m, returning -1 if so. If not, it computes the average, rounds it to the nearest integer, and then converts that integer to binary format.
*/

package main

import (
	"fmt"
	"math"
)

// RoundedAvg function
func RoundedAvg(n, m int) interface{} {
	if n > m {
		return -1
	}
	avg := math.Round(float64(n+m) / 2)
	return fmt.Sprintf("%b", int(avg))
}

func main() {
	fmt.Println(RoundedAvg(1, 5))
	fmt.Println(RoundedAvg(7, 5))
	fmt.Println(RoundedAvg(10, 20))
	fmt.Println(RoundedAvg(20, 33))
}

/*
Output:
11
-1
1111
11010
*/

/*
Explanation:

The function RoundedAvg(n, m int) interface{} takes two integers n and m as input.

If n is greater than m, it returns -1.

If n is not greater than m, it calculates the average of n and m, rounds it to the nearest integer, and then converts it to binary format.

The fmt.Sprintf("%b", int(avg)) line converts the rounded average to binary format.

The function returns the binary string.
*/
/*
