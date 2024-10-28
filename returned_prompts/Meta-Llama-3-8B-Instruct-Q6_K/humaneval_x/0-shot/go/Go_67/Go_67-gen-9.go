Here is the solution in Go:

```go
import (
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	// Remove the last character of the string
	s = s[:len(s)-1]

	// Split the string into two parts
	parts := strings.Split(s, " and ")

	// Convert the parts into integers
	apples, _ := strconv.Atoi(strings.Split(parts[0], " ")[0])
	oranges, _ := strconv.Atoi(strings.Split(parts[1], " ")[0])

	// Return the difference between the total fruits and the apples and oranges
	return n - apples - oranges
}
```


This function takes a string `s` that represents a number of apples and oranges distributed in a basket of fruit, and an integer `n` that represents the total number of fruits in the basket. It then returns the number of mango fruits in the basket. The function first removes the last character of the string to handle the " and " at the end. It then splits the string into two parts, converts them into integers, and returns the difference between the total fruits and the apples and oranges.