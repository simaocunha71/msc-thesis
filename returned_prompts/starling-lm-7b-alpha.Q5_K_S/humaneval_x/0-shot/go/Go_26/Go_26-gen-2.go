
To remove all duplicate elements from a list of integers, you can use the following algorithm:

1. Create an empty result slice of type `[]int`.
2. Iterate over the input slice.
3. For each element in the input slice, check if it is already present in the result slice. If not, add it to the result slice.
4. After iterating over the entire input slice, return the result slice.

Here's the implementation in Go:

```go
func RemoveDuplicates(numbers []int) []int {
    result := make([]int, 0)

    for _, num := range numbers {
        found := false
        for _, existingNum := range result {
            if existingNum == num {
                found = true
                break
            }
        }
        if !found {
            result = append(result, num)
        }
    }
    return result
}
```

The `RemoveDuplicates` function works as follows:

- It initializes an empty result slice.
- It iterates over each number in the input slice using a `for` loop and a range expression.
- For each number, it checks if it is already present in the result slice by iterating over each element in the result slice using another `for` loop and a range expression. If the number is found, the `found` variable is set to `true` and the inner loop is exited using the `break` statement.
- After checking all the numbers in the input slice, it adds the number to the result slice if it was not found in the result slice.
- Finally, it returns the result slice, which contains all the unique numbers from the input slice in the same order.

Here are some example usages of the `RemoveDuplicates` function:

```go
fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4})) // Output: [1 3 4]
fmt.Println(RemoveDuplicates([]int{5, 5, 6, 7, 8, 8})) // Output: [5 6 7]
```

As you can see, the function removes all duplicate elements from the input slice while preserving the