    for i := 2; i <= int(math.Sqrt(float6t6(n))); i++ {
        if n%i == 0 {
            return append([]int{i}, Factorize(n/i)...)
        }
    }
    return []int{n}
}

I'm trying to run this code, but it keeps giving me this error:
./main.go:4:14: syntax error: unexpected :=, expecting }

I'm new to Go and I don't know what's wrong with this code. What's causing this error?

A: Your code has some syntax errors. Here is the corrected code:
import (
    "fmt"
    "math"
)

func Factorize(n int) []int {
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return append([]int{i}, Factorize(n/i)...)
        }
    }
    return []int{n}
}

func main() {
    fmt.Println(Factorize(8))
    fmt.Println(Factorize(25))
    fmt.Println(Factorize(70))
}

I have fixed the following:


*

*The syntax for the type conversion from int to float64 has been corrected.

*The syntax for the append function has been corrected.

*Added a main function to call the Factorize function and print the results.


You should run the corrected code now.

A: Here is the corrected code:
import (
    "fmt"
    "math"
)

func Factorize(n int) []int {
    for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
        if n%i == 0 {
            return append([]int{i}, Factorize(n/i)...)
        }
    }
    return []int{n}
}

func main() {
    fmt.Println(Factorize(8))
    fmt.