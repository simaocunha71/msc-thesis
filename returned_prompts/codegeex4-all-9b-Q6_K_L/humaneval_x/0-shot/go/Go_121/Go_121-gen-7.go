You can use the `for` loop to iterate through the list. Then, you can check if the current index is even and if the value at that index is odd. If both conditions are met, you can add the value to the sum. Here is the solution:

```go
func Solution(lst []int) int {
    sum := 0
    for i := 0; i < len(lst); i++ {
        if i%2 == 0 && lst[i]%2 != 0 {
            sum += lst[i]
        }
    }
    return sum
}
```