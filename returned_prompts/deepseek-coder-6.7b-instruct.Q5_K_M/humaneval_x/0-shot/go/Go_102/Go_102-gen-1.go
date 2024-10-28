
    if x > y {
        return -1
    }

    if x%2 == 1 {
        x++
    }

    if x > y {
        return -1
    }

    return y
}
```

## Answer 2

```go
package main

import "fmt"

func ChooseNum(x, y int) int {
    if x%2 == 1 {
        x++
    }
    if x > y {
        return -1
    }
    return y - (y-x)%2
}

func main() {
    fmt.Println(ChooseNum(12, 15)) // 14
    fmt.Println(ChooseNum(13, 12)) // -1
}
```

## Answer 3

```go
package main

import (
	"fmt"
	"math"
)

// ChooseNum returns the biggest even number within the range [x, y]
func ChooseNum(x, y int) int {
	if x%2 == 1 {
		x++
	}
	if x > y {
		return -1
	}
	return y - (y-x)%2
}

func main() {
	fmt.Println(ChooseNum(12, 15)) // 14
	fmt.Println(ChooseNum(13, 12)) // -1
}
```

## Answer 4

```go
package main

import "fmt"

func ChooseNum(x, y int) int {
	if x%2 == 1 {
		x++
	}
	if x > y {
		return -1
	}
	return y - (y-x)%2
}

func main() {
	fmt.Println(ChooseNum(12, 15)) // 14
	fmt.Println(ChooseNum(13, 12)) // -1
}
```

## Answer 5

```go
package main

import "fmt"

func ChooseNum(x, y int) int {
	if x%2 == 1 {
		x++
