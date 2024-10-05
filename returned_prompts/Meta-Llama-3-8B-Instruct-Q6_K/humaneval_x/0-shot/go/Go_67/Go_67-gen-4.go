Here is a solution that uses regular expressions to extract the number of apples and oranges from the string, and then calculates the number of mangoes:

```go
package main

import (
	"fmt"
	"regexp"
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	re, _ := regexp.Compile(`(\d+) apples? and (\d+) oranges?`)
	matches := re.FindStringSubmatch(s)
	apples, _ := strconv.Atoi(matches[1])
	oranges, _ := strconv.Atoi(matches[2])
	return n - apples - oranges
}

func main() {
	fmt.Println(FruitDistribution("5 apples and 6 oranges", 19)) // Output: 8
	fmt.Println(FruitDistribution("0 apples and 1 oranges", 3)) // Output: 2
	fmt.Println(FruitDistribution("2 apples and 3 oranges", 100)) // Output: 95
	fmt.Println(FruitDistribution("100 apples and 1 oranges", 120)) // Output: 19
}
```

In this code, the `FruitDistribution` function uses a regular expression to extract the number of apples and oranges from the input string. The regular expression `(\d+) apples? and (\d+) oranges?` matches one or more digits followed by the words "apples" or "apples and", and then matches one or more digits followed by the words "oranges" or "oranges and". The `FindStringSubmatch` function returns the matched strings in a slice, and the `Atoi` function converts the strings to integers.

The function then subtracts the number of apples and oranges from the total number of fruits to get the number of mangoes. The result is returned by the function.

In the `main` function, the `FruitDistribution` function is called with different input strings and the total number of fruits, and the results are printed to the console.