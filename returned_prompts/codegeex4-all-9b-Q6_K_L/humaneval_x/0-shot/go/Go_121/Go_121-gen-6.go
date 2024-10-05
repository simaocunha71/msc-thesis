Here's the solution. This function iterates over the list and checks if the index of the current element is even and the element itself is odd. If both conditions are met, it adds the element to the sum. At the end, it returns the sum.

```go
func Solution(lst []int) int {
    sum := 0
    for i, num := range lst {
        if i % 2 == 0 && num % 2 == 1 {
            sum += num
        }
    }
    return sum
}
```

This solution has a time complexity of O(n), where n is the length of the list, and a space complexity of O(1), because it only uses a constant amount of space to store the sum.