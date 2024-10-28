	split_s := strings.Split(s, " ")
	apple, _ := strconv.Atoi(split_s[2])
	orange, _ := strconv.Atoi(split_s[5])

B:
	return n - apple - orange
}
```

## 3.1.2 

```go
// 3.1.2
package main

import (
	"fmt"
	"strconv"
	"strings"
)

func FruitDistribution(s string, n int) int {
	split_s := strings.Split(s, " ")
	apple, _ := strconv.Atoi(split_s[2])
	orange, _ := strconv.Atoi(split_s[5])

	return n - apple - orange
}

func main() {
	fmt.Println(FruitDistribution("5 apples and 6 oranges", 19)) // should print 8
	fmt.Println(FruitDistribution("0 apples and 1 oranges", 3))  // should print 2
	fmt.Println(FruitDistribution("2 apples and 3 oranges", 100)) // should print 95
	fmt.Println(FruitDistribution("100 apples