
To solve this problem, you can follow these steps:

1. Initialize a variable `maxEl` with the first element of the list `l`.
2. Iterate through the list `l` starting from the second element.
3. For each element in the list, check if it is greater than `maxEl`. If it is, update `maxEl` to that element.
4. After the iteration, `maxEl` will hold the maximum element in the list. Return `maxEl`.

Here's the implementation in Go:

```go
func MaxElement(l []int) int {
    maxEl := l[0]
    for i := 1; i < len(l); i++ {
        if l[i] > maxEl {
            maxEl = l[i]
        }
    }
    return maxEl
}
```

You can use the function by calling `MaxElement` with a slice of integers as the argument. The function will return the maximum element in the list.

Here are some examples:

```go
fmt.Println(MaxElement([]int{1, 2, 3}))  // Output: 3
fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))  // Output: 123
```

Note: The `fmt.Println` function is used here to print the result to the console. You can modify the code as per your requirements.

I hope this helps! Let me know if you have any more questions.

```go
package main

import "fmt"

func MaxElement(l []int) int {
    maxEl := l[0]
    for i := 1; i < len(l); i++ {
        if l[i] > maxEl {
            maxEl = l[i]
        }
    }
    return maxEl
}

func main() {
    fmt.Println(MaxElement([]int{1, 2, 3}))  // Output: 3
    fmt.Println(MaxElement([]int{5, 3, -5, 