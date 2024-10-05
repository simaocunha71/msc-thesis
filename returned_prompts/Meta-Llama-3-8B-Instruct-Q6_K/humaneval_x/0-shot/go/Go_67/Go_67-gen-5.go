Here is the solution for the problem:

```go
import (
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	// Split the input string by "and" to get the number of apples and oranges
	parts := strings.Split(s, "and")

	// Split the first part by " " to get the number of apples
	apples, _ := strconv.Atoi(strings.Split(parts[0], " ")[0])

	// Split the second part by " " to get the number of oranges
	oranges, _ := strconv.Atoi(strings.Split(parts[1], " ")[0])

	// Calculate the number of mango fruits
	mangoes := n - apples - oranges

	return mangoes
}
```


Explanation:

1. We split the input string `s` by "and" to get two parts, each representing the number of apples and oranges.
2. We split the first part by " " to get the number of apples and convert it to an integer using `strconv.Atoi`.
3. We split the second part by " " to get the number of oranges and convert it to an integer using `strconv.Atoi`.
4. We calculate the number of mango fruits by subtracting the number of apples and oranges from the total number of fruits `n`.
5. We return the number of mango fruits as an integer.