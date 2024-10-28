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


Here is the explanation:

1. We initialize a variable `sum` to store the sum of the odd elements in even positions.
2. We iterate over the list using a range-based for loop. In each iteration, we get the index `i` and the value `v` of the current element.
3. We check if the index `i` is even using the modulo operator `%`. If it is, we then check if the value `v` is odd using the modulo operator `%` again. If both conditions are true, we add the value to the `sum`.
4. Finally, we return the `sum` as the result.

The time complexity of this solution is O(n), where n is the length of the input list, because we iterate over the list once. The space complexity is O(1), because we only use a constant amount of space to store the `sum` variable.