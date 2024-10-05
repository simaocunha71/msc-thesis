You can solve this problem by using a for loop to iterate through the input list and append the delimeter and the current number to a new list. Here is a possible solution:

```go
func Intersperse(numbers []int, delimeter int) []int {
    // Create a new slice to store the result
    var result []int

    // Check if the input slice is empty
    if len(numbers) == 0 {
        return result
    }

    // Iterate through the input slice
    for i := 0; i < len(numbers); i++ {
        // If the current index is not the last one, append the delimeter and the current number to the result slice
        if i != len(numbers)-1 {
            result = append(result, delimeter, numbers[i])
        } else {
            // If the current index is the last one, just append the current number to the result slice
            result = append(result, numbers[i])
        }
    }

    return result
}
```

This solution has a time complexity of O(n), where n is the length of the input list.