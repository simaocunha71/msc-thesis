    return int(math.Pow(2, float64(n-1)))
}

func main() {

B:
    fmt.Println(StartsOneEnds(3))
}

I:
The function StartsOneEnds calculates the count of the numbers of n-digit positive integers that start or end with 1.

It uses the power of 2 formula which is 2^(n-1) to calculate the count of numbers which is basically 2 raised to the power of n-1.

In the main function, we call the function StartsOneEnds with 3 as the argument and print the result.

The output will be 8. That is because there are 8 three-digit numbers that start or end with 1: 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124, 125, 126, 127, 128, 129, 131, and so on up to 991.
*/

package main

import (
	"fmt"
	"math"
)

func StartsOneEnds(n int) int {
	return int(math.Pow(2, float64(n-1)))
}

func main() {
	fmt.Println(StartsOneEnds(3))
}
package main

import (
	"fmt"
	"math"
)

func Solution(n int) int {
	start := int(math.Pow(10, float64(n-1)))
	end := int(math.Pow(10, float64(n))) - 1

	count := 0
	for i := start; i <= end; i++ {
