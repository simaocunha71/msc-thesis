Here is the solution:

```go
import (
    "math"
)

func Compare(game, guess []int) []int {
    result := make([]int, len(game))
    for i, score := range game {
        result[i] = int(math.Abs(float64(score - guess[i])))
    }
    return result
}
```

This function takes two arrays `game` and `guess` as input and returns a new array where each element is the absolute difference between the corresponding elements in `game` and `guess`. The `math.Abs` function is used to calculate the absolute difference. The result is returned as a new array. 

The time complexity of this function is O(n), where n is the length of the input arrays, because it needs to iterate over each element in the arrays once. The space complexity is also O(n), because it needs to create a new array to store the result. 

You can use this function like this:

```go
game := []int{1, 2, 3, 4, 5, 1}
guess := []int{1, 2, 3, 4, 2, -2}
result := Compare(game, guess)
fmt.Println(result) // Output: [0 0 0 0 3 3]
``` 





This is the final answer. I hope it is correct.  Let me know if you have any further questions!