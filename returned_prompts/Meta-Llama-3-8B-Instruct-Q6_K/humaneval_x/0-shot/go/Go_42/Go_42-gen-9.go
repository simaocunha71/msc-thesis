```go
package main

import (
	"fmt"
	"math/rand"
	"time"
)

func IncrList(l []int) []int {
	for i, v := range l {
		l[i] = v + 1
	}
	return l
}

func main() {
	rand.Seed(time.Now().UnixNano())
	l := make([]int, 10)
	for i := range l {
		l[i] = rand.Intn(100)
	}
	fmt.Println("Before:", l)
	fmt.Println("After:", IncrList(l))
}
```

