Here is a Go function that implements the FruitDistribution task:
```go
package main

import (
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	// Split the string into parts
	parts := strings.Split(s, " ")

	// Extract the number of apples and oranges
	apples, _ := strconv.Atoi(parts[1][:strings.Index(parts[1], " ")])

	oranges, _ := strconv.Atoi(parts[3][:strings.Index(parts[3], " ")])

	// Calculate the number of mangoes
	mangoes := n - apples - oranges

	return mangoes
}

func main() {
	// Test cases
	fmt.Println(FruitDistribution("5 apples and 6 oranges", 19)) // 8
	fmt.Println(FruitDistribution("0 apples and 1 oranges", 3))   // 2
	fmt.Println(FruitDistribution("2 apples and 3 oranges", 100)) // 95
	fmt.Println(FruitDistribution("100 apples and 1 oranges", 120)) // 19
}
```
This function uses the `strings` package to split the input string into parts, and then uses the `strconv` package to convert the parts into integers. It then calculates the number of mangoes by subtracting the number of apples and oranges from the total number of fruits. The result is returned as an integer. In the `main` function, we test the `FruitDistribution` function with some sample inputs and print the results.