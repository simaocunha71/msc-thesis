```go
func Solution(lst []int) int {
    sum := 0
    for i, v := range lst {
        if i%2 == 0 && v%2 != 0 {
            sum += v
        }
    }
    return sum
}
```
Explanation:
The function `Solution` takes a slice of integers as input and returns the sum of all odd elements that are in even positions.

We initialize a variable `sum` to 0 to store the sum of the odd elements.

We iterate through the slice using a for loop and the range function, which returns the index `i` and the value `v` of each element in the slice.

We check if the index `i` is even (i.e., `i%2 == 0`) and if the value `v` is odd (i.e., `v%2 != 0`). If both conditions are true, we add the value `v` to the sum `sum`.

Finally, we return the sum `sum`.

For example, if the input is `[5, 8, 7, 1]`, the function will iterate through the slice as follows:

- `i=0`, `v=5`, `i%2 == 0` is true, `v%2 != 0` is true, so `sum` becomes `5`.
- `i=1`, `v=8`, `i%2 == 1` is true, `v%2 == 0` is true, so `sum` remains `5`.
- `i=2`, `v=7`, `i%2 == 0` is true, `v%2 != 0` is true, so `sum` becomes `12`.
- `i=3`, `v=1`, `i%2 == 1` is true, `v%2 != 0` is true, so `sum` remains `12`.

The function returns `12`, which is the sum of the odd elements that are in even positions.