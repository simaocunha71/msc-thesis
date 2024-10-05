
// initialize the 4 base cases
    if n == 0 {
        return 0
    } else if n == 1 {
        return 0
    } else if n == 2 {
        return 2
    } else if n == 3 {
        return 0
    }

B:

// initialize the variables for the last four numbers in the sequence
    a, b, c, d := 0, 0, 2, 0
    var next int

C:

// iterate over the rest of the sequence
    for i := 4; i <= n; i++ {
        next = a + b + c + d
        a, b, c, d = b, c, d, next
    }

D:

// return the nth number in the sequence
    return next
}

// Test cases
func main() {
    fmt.Println(Fib4(5)) // 4
    fmt.Println(Fib4(6)) // 8
    fmt.Println(Fib4(7)) // 14
}

// The solution has a time complexity of O(n) and a space complexity of O(1), because it only stores the last four numbers in the sequence and iterates through the rest of the sequence.
func main() {
    fmt.Println(Fib4(5)) // 4
    fmt.Println(Fib4(6)) // 8
    fmt.Println(Fib4(7)) // 14
}

// The solution has a time complexity of O(n) and a space complexity of O(1), because it only stores the last four numbers in the sequence and iterates through the rest of the sequence.
func main() {
    fmt.Println(Fib4(5)) // 4
    fmt.Println(Fib4(6)) // 8
    fmt.Println(Fib4(7)) // 14
}

// The solution has a time complexity of O(n) and a space complexity of O(1), because it only stores the last four numbers in the sequence and iterates through the rest of the sequence.
*/

import "fmt"

func Fib4(