```go
import (
	"math"
)

func Pluck(arr []int) []int {
    if len(arr) == 0 {
        return []int{}
    }

    smallestEven := math.MaxInt64
    smallestEvenIndex := -1

    for i, value := range arr {
        if value%2 == 0 && value < smallestEven {
            smallestEven = value
            smallestEvenIndex = i
        }
    }

    if smallestEvenIndex == -1 {
        return []int{}
    }

    return []int{smallestEven, smallestEvenIndex}
}
```
