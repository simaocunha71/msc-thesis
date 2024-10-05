// Your solution here
package main
import "fmt"

func Eat(number, need, remaining int) []int {
    if need > remaining {
        return []int{number + remaining, 0}
    } else {
        return []int{number + need, remaining - need}
    }
}

func main() {
    fmt.Println(Eat(5, 6, 10)) // [11, 4]
    fmt.Println(Eat(4, 8, 9)) // [12, 1]
    fmt.Println(Eat(1, 10, 10)) // [11, 0]
    fmt.Println(Eat(2, 11, 5)) // [7, 0]
}
// Output:
// [11 4]
// [12 1]
// [11 0]
// [7 0] 

// Your code should be able to handle these test cases. The code I wrote here is a simple and efficient solution that passes all test cases.