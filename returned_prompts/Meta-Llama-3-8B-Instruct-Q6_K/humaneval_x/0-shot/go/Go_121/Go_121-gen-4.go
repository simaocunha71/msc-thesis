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


The solution checks each element in the list to see if it is in an even position (i.e., `i%2 == 0`) and if it is odd (i.e., `lst[i]%2 != 0`). If both conditions are met, it adds the element to the sum. Finally, it returns the sum.