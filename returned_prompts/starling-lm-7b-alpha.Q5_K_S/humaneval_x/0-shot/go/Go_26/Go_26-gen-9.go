
To solve this problem, we can use a map to record the occurrence of each element in the input list. Then, we iterate through the input list and only add elements to the result list if they haven't occurred in the input list before.

Here's a step-by-step breakdown of the code:

1. We create an empty map called "seen" to keep track of the occurrence of each element.
2. We create an empty slice called "result" to store the elements that don't occur more than once.
3. We iterate through the input list using a for loop. For each number, we check if it is already in the "seen" map. If it's not, we add it to both the "seen" map and the "result" slice.
4. Finally, we return the "result" slice, which contains all the unique elements in the order they appear in the input list.

Here's the code for the solution:

```go
func RemoveDuplicates(numbers []int) []int {
    seen := make(map[int]bool)
    result := make([]int, 0)

    for _, number := range numbers {
        if !seen[number] {
            seen[number] = true
            result = append(result, number)
        }
    }

    return result
}
```

When you call the `RemoveDuplicates` function with the input `[1, 2, 3, 2, 4]`, it will return `[1, 3, 4]`.

This solution has a time complexity of O(n) because we only iterate through the input list once, and a space complexity of O(n) because we store all the unique elements in the "result" slice.

Note: The `:=` operator is used to declare and assign a variable in a single step. It's equivalent to `var result []int; result = make([]int, 0)`.

In Go, the range expression in a for loop is evaluated once at the beginning of the loop. The variable `number` takes the value of each element in the `numbers` slice in each iteration of the loop.

The expression `!seen[number]` checks if the element `number`