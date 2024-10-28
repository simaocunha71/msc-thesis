The solution is to iterate over the list, and for each element, check if it is odd and if its index is even. If both conditions are met, add the element to the sum. The index of an element in a list can be found using the index function.

Here is the modified solution:

```go
func Solution(lst []int) int {
    sum := 0
    for i, v := range lst {
        if i % 2 == 0 && v % 2 != 0 {
            sum += v
        }
    }
    return sum
}
```

This solution works by iterating over the list, and for each element, checking if its index is even and if the element itself is odd. If both conditions are met, the element is added to the sum. The result is then returned.

In the example, the list [5, 8, 7, 1] is passed to the solution. The first element (5) has an odd value and an even index, so it is added to the sum. The second element (8) has an even value and an even index, so it is not added to the sum. The third element (7) has an odd value and an even index, so it is added to the sum. The fourth element (1) has an odd value and an odd index, so it is not added to the sum. The sum is then returned, which is 12.