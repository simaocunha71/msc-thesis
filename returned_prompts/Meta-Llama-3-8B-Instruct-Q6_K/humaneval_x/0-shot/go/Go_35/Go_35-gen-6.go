package main
import "fmt"

// Return maximum element in the list.
// >>> MaxElement([1, 2, 3])
// 3
// >>> MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
// 123
func MaxElement(l []int) int {
    var max int
    for _, v := range l {
        if v > max {
            max = v
        }
    }
    return max
}

func main() {
    fmt.Println(MaxElement([]int{1, 2, 3})) // Output: 3
    fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // Output: 123
}
B:
package main
import "fmt"

// Return maximum element in the list.
// >>> MaxElement([1, 2, 3])
// 3
// >>> MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
// 123
func MaxElement(l []int) int {
    return int(MaxInt(float64(Max(l))))
}

func MaxInt(f float64) float64 {
    max := f
    for _, v := range l {
        if float64(v) > max {
            max = float64(v)
        }
    }
    return max
}

func Max(l []int) []int {
    var max []int
    for _, v := range l {
        max = append(max, v)
    }
    return max
}

func main() {
    fmt.Println(MaxElement([]int{1, 2, 3})) // Output: 3
    fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // Output: 123
}
C:
package main
import "fmt"

// Return maximum element in the list.
// >>> MaxElement([1, 2, 3])
// 3
// >>> MaxElement([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10