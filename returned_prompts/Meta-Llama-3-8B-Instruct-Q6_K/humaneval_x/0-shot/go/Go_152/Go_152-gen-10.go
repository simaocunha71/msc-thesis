Here is the solution:

```go
func Compare(game, guess []int) []int {
    result := make([]int, len(game))
    for i := range game {
        result[i] = int(math.Abs(float64(guess[i] - game[i])))
    }
    return result
}
```

This function creates a new slice of the same length as the input slices and then iterates over the input slices, calculating the absolute difference between the guess and the game score at each position and storing this value in the new slice. The result is then returned. 

The math.Abs function is used to get the absolute value of the difference, which ensures that the result is always non-negative, and the float64 conversion is used to allow the calculation of the absolute value of a float64 value. 

This function assumes that the input slices are of the same length and that the input values are all integers. If the input values are not integers, you will need to convert them to integers before calculating the absolute difference. 

Also note that this function will return a slice of the same length as the input slices, where each element of the slice is the absolute difference between the guess and the game score at the corresponding position. If the guess is correct, the absolute difference will be 0, and if not, it will be the absolute difference between the guess and the game score. 

This function does not check if the input values are within a certain range or if the input slices are of the same length. You may want to add error checking code to handle these cases if they are possible. 

The example usage of this function is:

```go
game := []int{1,2,3,4,5,1}
guess := []int{1,2,3,4,2,-2}
result := Compare(game, guess)
fmt.Println(result)  // prints [0 0 0 0 3 3]
```

This code will print the result of the comparison between the game scores and the guesses. The first four elements of the result slice will be 0, indicating that the guesses were correct, and the last two elements will be 3, indicating that the guesses were 3 away from the actual scores. 