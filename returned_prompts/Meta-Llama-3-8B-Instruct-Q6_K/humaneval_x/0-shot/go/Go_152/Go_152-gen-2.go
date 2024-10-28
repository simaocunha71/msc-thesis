Here is a simple solution in Go:

```go
import (
    "math"
)

func Compare(game, guess []int) []int {
    result := make([]int, len(game))
    for i, g := range game {
        result[i] = int(math.Abs(float64(g - guess[i])))
    }
    return result
}
```

This function uses the `math.Abs` function to calculate the absolute difference between each guess and the corresponding score. The result is stored in a new array which is returned at the end. The `make` function is used to create a new array of the same length as the input arrays. The `range` keyword is used to iterate over the input arrays. The `int` conversion is used to convert the float64 result of `math.Abs` to an integer. 

This solution has a time complexity of O(n), where n is the length of the input arrays. This is because it iterates over the input arrays once. The space complexity is also O(n), as it creates a new array of the same length as the input arrays. 