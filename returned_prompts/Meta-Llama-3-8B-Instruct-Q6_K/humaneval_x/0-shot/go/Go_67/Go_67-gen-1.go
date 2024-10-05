You can solve this problem by parsing the input string to extract the number of apples and oranges, and then subtracting them from the total number of fruits. Here's a possible implementation in Go:
```go
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	// Split the string into two parts: the first part is the apples, the second part is the oranges
	parts := strings.Split(s, " and ")
	apples, _ := strconv.Atoi(strings.Split(parts[0], " ")[0])
	oranges, _ := strconv.Atoi(strings.Split(parts[1], " ")[0])

	// Calculate the number of mangoes
	mangoes := n - apples - oranges

	return mangoes
}

func main() {
	fmt.Println(FruitDistribution("5 apples and 6 oranges", 19)) // Output: 8
	fmt.Println(FruitDistribution("0 apples and 1 oranges", 3)) // Output: 2
	fmt.Println(FruitDistribution("2 apples and 3 oranges", 100)) // Output: 95
	fmt.Println(FruitDistribution("100 apples and 1 oranges", 120)) // Output: 19
}
```
This implementation uses the `strings.Split` function to split the input string into two parts, and then uses the `strconv.Atoi` function to convert the parts into integers. The number of mangoes is then calculated by subtracting the number of apples and oranges from the total number of fruits.

Note that this implementation assumes that the input string is in the format "x apples and y oranges", where x and y are integers. If the input string is in a different format, you may need to modify the implementation accordingly. Also, this implementation does not handle errors, so you may want to add error handling if you expect the input string to be invalid.