To solve this problem, you can follow these steps:

1. Initialize a variable `totalEaten` to store the total number of carrots Eaten.
2. Initialize a variable `leftover` to store the number of carrots left after your meals.
3. Subtract the `number` from the `need` and store the result in `leftover`.
4. Add the `need` to the `totalEaten`.
5. If `leftover` is greater than 0, subtract the `leftover` from the `remaining` and store the result in `leftover`.
6. If `remaining` is greater than 0, add the `remaining` to the `totalEaten`.
7. Return an array of `totalEaten` and `leftover`.

Here is an example implementation of the solution in Go:

```go
func Eat(number, need, remaining int) []int {
    totalEaten := number + need
    leftover := need - number

    if leftover > 0 {
        leftover = remaining - leftover
    }

    if remaining > 0 {
        totalEaten += remaining
    }

    return []int{totalEaten, leftover}
}
```

This solution first calculates the total number of carrots Eaten by adding the `number` and `need`. It then calculates the number of carrots left after your meals by subtracting the `number` from the `need`. If there are still leftover carrots, it subtracts them from the `remaining` variable. Finally, it adds any remaining carrots to the `totalEaten` variable. The function returns an array of the `totalEaten` and `leftover` variables.

You can test this function with the provided examples to see if it produces the correct results.

```go
fmt.Println(Eat(5, 6, 10)) // [11, 4]
fmt.Println(Eat(4, 8, 9)) // [12, 1]
fmt.Println(Eat(1,