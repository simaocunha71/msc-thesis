```go
package main

import "fmt"

func Add(lst []int) int {
    var sum int
    for i, v := range lst {
        if i%2 != 0 && v % 2 == 0 {
            sum += v
        }
    }
    return sum
}

func main() {
    fmt.Println(Add([]int{4, 2, 6, 7}))  // Output: 2
}
```



Explanation:
The task is to add the even elements in the list that are at odd indices. Here's how to do it:

1. Initialize a variable `sum` to store the sum of the even elements.

2. Iterate over the list using a for loop with a range. The range variable `i` will take the index of the element and `v` will take the value of the element.

3. Check if the index `i` is odd (`i % 2 != 0`) and the value `v` is even (`v % 2 == 0`). If both conditions are true, add the value `v` to the `sum`.

4. Finally, return the `sum`.

In the main function, we call the `Add` function with the list `[4, 2, 6, 7]` and print the result, which is `2`. The even elements at odd indices are `2` and `6`, and their sum is `2`.