
To remove all elements that occur more than once from a given list of integers, you can follow these steps:

1. Create a new empty slice called "seen" to keep track of the elements we have encountered so far. Initialize it as a map with integer keys and boolean values, representing the elements and whether they are seen or not.
2. Iterate over the input slice "numbers" using a for loop. For each element in the slice, check if it is already in the "seen" map.
3. If the element is not in the "seen" map, add it to the "seen" map with the value true, indicating that it is seen. Then, append the element to a new slice called "result".
4. If the element is already in the "seen" map and its value is false (indicating that it is not seen), update its value to true and append the element to the "result" slice.
5. After iterating through all the elements in the input slice, return the "result" slice, which will contain only the unique elements in the same order as they appeared in the input slice.

Here's the code for the RemoveDuplicates function in Go:

```go
func RemoveDuplicates(numbers []int) []int {
    seen := make(map[int]bool)
    result := []int{}
    
    for _, number := range numbers {
        if _, exists := seen[number]; !exists {
            seen[number] = true
            result = append(result, number)
        } else {
            seen[number] = true
        }
    }
    
    return result
}
```

You can use the RemoveDuplicates function like this:

```go
numbers := []int{1, 2, 3, 2, 4}
result := RemoveDuplicates(numbers)
fmt.Println(result) // Output: [1 3 4]
```

This will remove all duplicate elements from the "numbers" slice and return a new slice with only the unique elements in the same order as they appeared in the input slice.

Note: It's important to note that the order of the elements in the "result" slice is maintained because we append the elements to the "result"