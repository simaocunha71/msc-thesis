Here is the solution in Go:
```go
import (
    "strconv"
)

func AddElements(arr []int, k int) int {
    sum := 0
    for i := 0; i < k; i++ {
        str := strconv.Itoa(arr[i])
        if len(str) <= 2 {
            num, _ := strconv.Atoi(str)
            sum += num
        }
    }
    return sum
}
```
Here's an explanation of the code:

1. We initialize a variable `sum` to 0, which will store the sum of the elements with at most two digits.
2. We loop through the first `k` elements of the array using a for loop.
3. For each element, we convert it to a string using `strconv.Itoa(arr[i])`.
4. We check if the length of the string is less than or equal to 2 using `len(str) <= 2`. If it is, we know the element has at most two digits.
5. We convert the string back to an integer using `strconv.Atoi(str)` and add it to the `sum` variable.
6. Finally, we return the `sum` variable.

You can test this function with the example input you provided:
```go
arr := []int{111, 21, 3, 4000, 5, 6, 7, 8, 9}
k := 4
result := AddElements(arr, k)
fmt.Println(result) // Output: 24
```