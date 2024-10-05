You can solve this problem by using a map to keep track of the occurrences of each number in the list. Then, iterate over the list again and only add the numbers that appear once to a new list. Here's an example implementation in Go:

```go
func RemoveDuplicates(numbers []int) []int {
    // Create a map to keep track of occurrences
    occurrences := make(map[int]bool)
    // Create a new list to store the result
    result := make([]int, 0)

    // Iterate over the input list
    for _, number := range numbers {
        // Check if the number has already occurred
        if !occurrences[number] {
            // If it hasn't occurred, add it to the result list
            result = append(result, number)
            // Mark the number as occurred
            occurrences[number] = true
        }
    }

    // Return the result list
    return result
}
```

You can then call the function with a list of integers to remove duplicates:

```go
numbers := []int{1, 2, 3, 2, 4}
result := RemoveDuplicates(numbers)
fmt.Println(result) // Output: [1, 3, 4]
```