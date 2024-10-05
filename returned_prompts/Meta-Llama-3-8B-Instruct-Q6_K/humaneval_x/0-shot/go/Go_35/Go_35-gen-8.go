// We can use the built-in function max() from the package "math/big" to find the maximum element in the list.
package main
import "fmt"
import "math/big"

func MaxElement(l []int) int {
    var max = big.NewInt(0)
    for _, v := range l {
        if v.Int64() > max.Int64() {
            max = big.NewInt(int64(v))
        }
    }
    return int(max.Int64())
}

func main() {
    fmt.Println(MaxElement([]int{1, 2, 3}))         // 3
    fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // 123
}

B:
// We can use the built-in function max() from the package "math/big" to find the maximum element in the list.
package main
import "fmt"
import "math/big"

func MaxElement(l []int) int {
    var max = big.NewInt(0)
    for _, v := range l {
        if v > max {
            max = big.NewInt(int64(v))
        }
    }
    return int(max.Int64())
}

func main() {
    fmt.Println(MaxElement([]int{1, 2, 3}))         // 3
    fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // 123
}
C:
// We can use the built-in function max() from the package "math/big" to find the maximum element in the list.
package main
import "fmt"
import "math/big"

func MaxElement(l []int) int {
    var max = big.NewInt(0)
    for _, v := range l {
        if v > max {
            max = big.NewInt(int64(v))
        }
    }
    return int(max.Int64())
}

func main() {
    fmt.Println(MaxElement([]int{1, 2, 3}))         // 3
    fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // 123
}
D:
// We can use the built-in function max() from