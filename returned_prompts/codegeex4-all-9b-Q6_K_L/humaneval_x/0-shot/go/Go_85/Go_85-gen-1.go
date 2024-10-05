The problem requires summing up the even elements that are located at odd indices in a given slice of integers. 

Here is a possible solution using Go:

```go
func Add(lst []int) int {
    total := 0
    for i := 1; i < len(lst); i += 2 {
        if lst[i]%2 == 0 {
            total += lst[i]
        }
    }
    return total
}
```

In this solution, we iterate over the slice starting from index 1 (the first odd index) and increment by 2 in each iteration to reach the next odd index. We check if the element at the current odd index is even by using the modulus operator `%`. If it is even, we add it to the `total` variable. Finally, we return the `total`.