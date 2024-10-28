// simplify the expression
// x * n = (x_num * n_num) / (x_denom * n_denom)
// if x * n is a whole number, return true; else return false
x_simplify := (x_num * n_num) / (x_denom * n_denom)
n_simplify := (n_num * x_num) / (n_denom * x_denom)

if x_simplify == n_simplify {
    return true
}
return false


A: You can simplify the expression x * n by multiplying the numerators and the denominators separately and then simplifying the result. The code below shows the implementation:

```go
import (
    "strconv"
    "strings"
)

func Simplify(x, n string) bool {
    // Split x and n by '/'
    xSplit := strings.Split(x, "/")
    nSplit := strings.Split(n, "/")

    // Convert string to int
    xNum, _ := strconv.Atoi(xSplit[0])
    xDenom, _ := strconv.Atoi(xSplit[1])