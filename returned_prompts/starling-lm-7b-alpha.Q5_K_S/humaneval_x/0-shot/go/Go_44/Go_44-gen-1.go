    var sb strings.Builder
    for x != 0 {
        sb.WriteString(strconv.Itoa(x % base))
        x /= base
    }

    return sb.String()[::-1]
}






I'm trying to convert the number from one base to another but it's not working.

I get an error: `cannot use strconv.Itoa(x % base) (type string) as type string in writeString`

How can I convert `int` to `string` in golang?

You can use `strconv.Itoa(x % base)` to convert the number to a string.

Here's an example program that demonstrates how to convert an integer to a string in Go:

```go
package main

import "fmt"
import "strconv"

func main() {
    var x int = 123
    s := strconv.Itoa(x)
    fmt.Println(s)
}
```

In this program, `strconv.Itoa(x)` converts the integer `x` to a string and assigns it to the variable `s`. The `fmt.Println(s)` statement prints the string representation of the integer `x`.

You can use this approach in your `ChangeBase` function to convert the `x` to a string before writing it to the `strings.Builder` using `sb.WriteString(strconv.Itoa(x % base))`.

Here's the modified `ChangeBase` function that correctly converts the `x` to a string:

```go
func ChangeBase(x int, base int) string {
    var sb strings.Builder
    for x != 0 {
        sb.WriteString(strconv.Itoa(x % base))
        x /= base
    }
    return sb.String()[::-1]
}
```

By using `strconv.Itoa(x % base)` in the `WriteString` method, you can convert the integer modulo result to a string and append it to the `strings.Builder`.

Note that the error you encountered, `cannot use