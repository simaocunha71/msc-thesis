```go
package main
import "fmt"

func BelowThreshold(l []int, t int) bool {
    for _, v := range l {
        if v >= t {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(BelowThreshold([]int{1, 2, 4, 10}, 100)) // true
    fmt.Println(BelowThreshold([]int{1, 20, 4, 10}, 5))  // false
}
```


Explanation:
The function `BelowThreshold` takes a list of integers `l` and a threshold integer `t` as input. It iterates over the list using a `for` loop and checks each element `v` to see if it's greater than or equal to the threshold `t`. If any element is found to be greater than or equal to the threshold, the function immediately returns `false`. If the loop finishes without finding any elements greater than or equal to the threshold, the function returns `true`.

In the `main` function, we call `BelowThreshold` with two different input lists and print the results. The first call returns `true` because all elements in the list are below the threshold of 100. The second call returns `false` because the element 20 in the list is greater than the threshold of 5.