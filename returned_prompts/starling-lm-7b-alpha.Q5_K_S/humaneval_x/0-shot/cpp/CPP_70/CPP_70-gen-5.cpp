
Here is a sample implementation in Go:

```go
package main

import "fmt"

func GetPositive(l []int) []int {
    result := []int{}
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}

func main() {
    fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6}))
    fmt.Println(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}
```

The `GetPositive` function takes in a slice of integers (`l`) and returns a new slice containing only the positive numbers. It does this by iterating over each element in the input slice using a `for` loop and checking if the element is greater than zero using the `>` operator. If the element is positive, it is appended to the `result` slice using the `append` function. Finally, the `result` slice is returned.

In the `main` function, the `GetPositive` function is called with two sample input slices and the returned slices are printed using the `fmt.Println` function.

The output of the program will be:
```
[2 5 6]
[5 3 2 3 9 123 1]
```

This means that the `GetPositive` function successfully filtered out the negative numbers from the input slices and returned only the positive numbers.

I hope this helps! Let me know if you have any more questions.

```go
package main

import "fmt"

func GetPositive(l []int) []int {
    result := []int{}
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}

func main() {
    fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6}))
    fmt.Println(