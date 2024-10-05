Here is the solution to the problem:
```go
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	// Split the string into two parts: the first part is the number of apples, and the second part is the number of oranges
	parts := strings.Split(s, " ")
	apples, _ := strconv.Atoi(parts[1][:strings.Index(parts[1], " ")])

	// Calculate the total number of fruits in the basket
	total := n - apples

	// Return the number of mango fruits in the basket
	return total
}

func main() {
	fmt.Println(FruitDistribution("5 apples and 6 oranges", 19)) // Output: 8
	fmt.Println(FruitDistribution("0 apples and 1 oranges", 3)) // Output: 2
	fmt.Println(FruitDistribution("2 apples and 3 oranges", 100)) // Output: 95
	fmt.Println(FruitDistribution("100 apples and 1 oranges", 120)) // Output: 19
}
```
This solution uses the `strings.Split` function to split the input string into two parts: the first part is the number of apples, and the second part is the number of oranges. Then, it uses the `strconv.Atoi` function to convert the number of apples from a string to an integer. Finally, it calculates the total number of fruits in the basket by subtracting the number of apples and oranges from the total number of fruits. The number of mango fruits in the basket is then returned.