```go
package main

import (
	"math"
)

func Compare(game, guess []int) []int {
	result := make([]int, len(game))
	for i, v := range game {
		result[i] = int(math.Abs(float64(guess[i] - v)))
	}
	return result
}

func main() {
	game := []int{1, 2, 3, 4, 5, 1}
	guess := []int{1, 2, 3, 4, 2, -2}
	fmt.Println(Compare(game, guess)) // Output: [0 0 0 0 3 3]
}
```
The `Compare` function takes two arrays, `game` and `guess`, as input. It initializes a new array `result` of the same length as `game`. Then it iterates over the `game` array, calculates the absolute difference between the current game score and the corresponding guess, and stores the result in the `result` array. Finally, it returns the `result` array. The `main` function demonstrates the usage of the `Compare` function with example inputs. The output is `[0 0 0 0 3 3]`, indicating that the guesses were correct for the first four matches and off by 3 for the last two matches.