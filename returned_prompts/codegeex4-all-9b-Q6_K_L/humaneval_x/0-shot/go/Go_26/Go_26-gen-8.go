You can use a map to keep track of the elements that have already been seen. Then, iterate through the input list and append only the elements that have not been seen to the result list. This will maintain the order of elements.

Here's the Go code that implements this logic:

```go
func RemoveDuplicates(numbers []int) []int {
	seen := make(map[int]bool)
	result := make([]int, 0)

	for _, num := range numbers {
		if !seen[num] {
			seen[num] = true
			result = append(result, num)
		}
	}

	return result
}
```

This code first creates a map called `seen` to keep track of the numbers that have been seen. Then, it creates an empty slice called `result` to store the result. 

Next, it iterates through the input list `numbers` using a range loop. For each number, it checks if the number has already been seen by looking it up in the `seen` map. If the number has not been seen, it adds it to the `seen` map and appends it to the `result` slice.

Finally, it returns the `result` slice, which contains only the elements that have not been seen more than once.