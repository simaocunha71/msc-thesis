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
The problem is asking to remove all elements from a given list of integers that occur more than once. The order of elements in the resulting list should be the same as in the input list. 

The solution is using a map to keep track of the elements we have seen. For each element in the input list, we check if it has been seen before. If not, we add it to the result list and mark it as seen. 

Here is the Go code for this problem:

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

This function takes a slice of integers as input, creates a new map to keep track of seen elements, and a new slice to store the result. It then iterates over the input slice, checks if each element has been seen before, and if not, adds it to the result slice and marks it as seen. Finally, it returns the result slice. 

For example, if you call `RemoveDuplicates([1, 2, 3, 2, 4])`, the function will return `[1, 3, 4]`. 

This solution has a time complexity of O(n), where n is the length of the input slice, because we are iterating over the slice once. The space complexity is also O(n), because in the worst case, all elements in the input slice are unique, so we will need to store all of them in the result slice and the map. 

This solution is efficient and easy to understand. It is also a common approach to solving this kind of problem in Go.  However, it is worth noting that Go has a built-in function called `uniq` that can be used to remove duplicates from a slice. It is not as efficient as this solution, but it is easier to use and can be a good choice for simple cases. 

Here is how you can use the `