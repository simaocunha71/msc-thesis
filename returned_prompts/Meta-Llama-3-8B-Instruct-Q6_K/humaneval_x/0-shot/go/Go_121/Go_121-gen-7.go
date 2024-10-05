```go
func Solution(lst []int) int {
    sum := 0
    for i, num := range lst {
        if i%2 == 0 && num % 2 != 0 {
            sum += num
        }
    }
    return sum
}
```



Solution:
```go
func Solution(lst []int) int {
    sum := 0
    for i, num := range lst {
        if i%2 == 0 && num % 2 != 0 {
            sum += num
        }
    }
    return sum
}
```

Explanation:
The function `Solution` takes a list of integers as input and returns the sum of all odd elements that are in even positions.

The function uses a for loop to iterate over the input list. For each element, it checks if the position (i) is even and the element is odd (num % 2 != 0). If both conditions are true, it adds the element to the sum.

The function returns the sum of all odd elements that are in even positions.

For example, for the input `[5, 8, 7, 1]`, the function returns `12` because the odd elements `5` and `7` are in even positions. For the input `[3, 3, 3, 3, 3]`, the function returns `9` because all the odd elements are in even positions. For the input `[30, 13, 24, 321]`, the function returns `0` because there are no odd elements in even positions.