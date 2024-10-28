Here is a simple Go function that accomplishes the task:

```go
import (
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	words := strings.Split(s, " ")
	apples, _ := strconv.Atoi(words[1][:strings.Index(words[1], " ")])
	oranges, _ := strconv.Atoi(words[3][:strings.Index(words[3], " ")])
	return n - apples - oranges
}
```

This function splits the input string into words, extracts the numbers of apples and oranges from the words, and then subtracts these numbers from the total number of fruits. The result is the number of mango fruits in the basket. Note that this function assumes that the input string is in the correct format and that the numbers of apples and oranges are valid integers. If these assumptions are not valid, the function may not work correctly.