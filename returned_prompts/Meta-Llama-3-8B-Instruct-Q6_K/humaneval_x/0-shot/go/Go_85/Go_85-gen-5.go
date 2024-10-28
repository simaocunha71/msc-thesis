```go
package main

import (
    "fmt"
)

func Add(lst []int) int {
    var sum int
    for i, v := range lst {
        if i%2 != 0 && v%2 == 0 {
            sum += v
        }
    }
    return sum
}

func main() {
    fmt.Println(Add([]int{4, 2, 6, 7})) // Output: 2
}
```

Explanation:
The function `Add` takes a list of integers `lst` as input and returns the sum of even elements that are at odd indices. 

We initialize a variable `sum` to 0. Then, we iterate over the list using a range-based for loop. For each element, we check if the index `i` is odd (`i%2 != 0`) and if the element is even (`v%2 == 0`). If both conditions are met, we add the element to the `sum`. 

Finally, we return the `sum`. 

In the `main` function, we test the `Add` function with the input `[4, 2, 6, 7]` and print the result, which is `2`. 

Note that the indices are 0-based, so the first element is at index 0, the second element is at index 1, and so on. Therefore, an index is considered odd if it is not divisible by 2. 

This function will work correctly for any list of integers and will return the sum of even elements at odd indices. 