
    var maxNumber = math.MinInt64
    var rollingMax = make([]int, len(numbers))

    for i, number := range numbers {
        if number > maxNumber {
            maxNumber = number
        }
        rollingMax[i] = maxNumber
    }

    return rollingMax
}

// From a given list of integers, generate a list of rolling minimum element found until given moment
// in the sequence.
// >>> RollingMin([1, 2, 3, 2, 3, 4, 2])
// [1, 1, 1, 1, 1, 1, 1]
func RollingMin(numbers  []int)  []int {

    var minNumber = math.MaxInt64
    var rollingMin = make([]int, len(numbers))

    for i, number := range numbers {
        if number < minNumber {
            minNumber = number
        }
        rollingMin[i] = minNumber
    }

    return rollingMin
}
```

## Testing

```go
package main

import (
    "fmt"
)

func main() {
    numbers := []int{1, 2, 3, 2, 3, 4, 2}
    fmt.Println(RollingMax(numbers)) // [1, 2, 3, 3, 3, 4, 4]
    fmt.Println(RollingMin(numbers)) // [1, 1, 1, 1, 1, 1, 1]
}
```

## Conclusion

Both solutions are straightforward, with the Max function iterating over the slice and updating the rolling maximum whenever a new maximum is found, and the Min function doing the same with the minimum value.

The time complexity of both solutions is O(n), where n is the number of elements in the slice. This is because each function has to traverse the slice once. The space complexity is O(n) as well, because of the space required for the rolling maximum and minimum slices.

This problem is a good example of how to use the built-in `