```go
package main
import "fmt"
func Monotonic(l []int) bool {
    inc := true
    dec := true
    for i := 1; i < len(l); i++ {
        if l[i] > l[i-1] {
            dec = false
        } else if l[i] < l[i-1] {
            inc = false
        }
    }
    return inc || dec
}
func main() {
    fmt.Println(Monotonic([]int{1, 2, 4, 20}))  // true
    fmt.Println(Monotonic([]int{1, 20, 4, 10})) // false
    fmt.Println(Monotonic([]int{4, 1, 0, -10})) // true
}
```

Explanation:
The function `Monotonic` checks if the elements in the given list `l` are either monotonically increasing or decreasing.

It uses two boolean variables `inc` and `dec` to track whether the list is increasing or decreasing. Initially, both `inc` and `dec` are set to `true`.

It then iterates over the list, starting from the second element (index 1), and checks if the current element is greater than the previous one. If it is, it sets `dec` to `false`. If it is less, it sets `inc` to `false`.

After the loop, it returns whether either `inc` or `dec` is `true`, indicating whether the list is monotonically increasing or decreasing.

In the `main` function, we test the `Monotonic` function with three different lists and print the results. The output confirms that the function correctly identifies monotonically increasing and decreasing lists.