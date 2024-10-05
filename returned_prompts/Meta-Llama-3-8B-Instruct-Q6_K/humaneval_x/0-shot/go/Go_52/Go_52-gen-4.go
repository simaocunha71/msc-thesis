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
    fmt.Println(BelowThreshold([]int{1, 2, 4, 10}, 100))  // true
    fmt.Println(BelowThreshold([]int{1, 20, 4, 10}, 5))   // false
}
```



Output:

```
true
false
```



Explanation:

The `BelowThreshold` function takes a slice of integers `l` and an integer `t` as input. It iterates over the slice using a range-based for loop and checks if each element `v` is greater than or equal to the threshold `t`. If any element is found to be greater than or equal to `t`, the function immediately returns `false`. If the loop completes without finding any elements greater than or equal to `t`, the function returns `true`.

In the `main` function, we test the `BelowThreshold` function with two different inputs. The first call checks if all numbers in the list `[1, 2, 4, 10]` are below the threshold `100`, which is true. The second call checks if all numbers in the list `[1, 20, 4, 10]` are below the threshold `5`, which is false. The output of both calls is printed to the console.