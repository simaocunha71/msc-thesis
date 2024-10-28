	a:= strings.Fields(s)
	apple, _ := strconv.Atoi(a[0])
	orange, _ := strconv.Atoi(a[2])

B:
	return n - apple - orange
}

// Tests
func main() {
	println(FruitDistribution("5 apples and 6 oranges", 19))  // Expected output 8
	println(FruitDistribution("0 apples and 1 oranges",3))   // Expected output 2
	println(FruitDistribution("2 apples and 3 oranges", 100)) // Expected output 95
	println(FruitDistribution("100 apples and 1 oranges",120)) // Expected output 19
}

The test cases are written in such a way that the function is expected to return the number of mango fruits in the basket. The function takes in two parameters, a string that describes the number of apples and oranges and an integer that represents the total number of fruits in the basket. The function then calculates and returns the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits.
*/

package main

import (
	"strconv"
	"strings"
)

// In this task, you will be given a string that represents a number of apples and oranges
// that are distributed