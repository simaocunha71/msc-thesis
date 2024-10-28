Here is a simple and efficient solution in Go:
```go
func RemoveDuplicates(numbers []int) []int {
    seen := make(map[int]bool)
    result := make([]int, 0, len(numbers))
    for _, num := range numbers {
        if !seen[num] {
            seen[num] = true
            result = append(result, num)
        }
    }
    return result
}
```
Here's an explanation of the code:

1. We create an empty map `seen` to keep track of the numbers we've seen so far.
2. We create an empty slice `result` to store the unique numbers.
3. We iterate through the input slice `numbers`.
4. For each number, we check if it's already in the `seen` map. If it's not, we add it to the `seen` map and append it to the `result` slice.
5. Finally, we return the `result` slice.

This solution has a time complexity of O(n), where n is the length of the input slice, because we're iterating through the slice once. The space complexity is also O(n), because we're storing the unique numbers in the `result` slice and the `seen` map.

You can test this function with the example input you provided:
```go
numbers := []int{1, 2, 3, 2, 4}
result := RemoveDuplicates(numbers)
fmt.Println(result) // [1, 3, 4]
```
I hope this helps! Let me know if you have any questions.