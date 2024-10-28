    result := ""
    if x < base {
        return strconv.Itoa(x)
    } else {
        result = strconv.Itoa(x % base) + result
        return ChangeBase(x / base, base) + result
    }
}

I'm trying to solve a problem in Go where I have to convert a given number to a specific base. This is a recursive function where the base number is less than 10.

A: I suggest using a more idiomatic way of handling this with slices. Here is how you can do it:

```go
package main

import (
    "fmt"
    "strconv"
)

func ChangeBase(x int, base int) string {
    var digits []string
    for x > 0 {
        digit := strconv.Itoa(x % base)
        digits = append(digits, digit)
        x = x / base
    }
    // Reverse the digits slice and join them into a single string.
    for i := len(digits)/2 - 1; i >= 0; i-- {
        opp := len(digits) - 1 - i
        digits[i], digits[opp] = digits[opp], digits[i]
    }
    return strings.Join(digits, "")
}

func main() {
    fmt.Println(ChangeBase(8, 3))
    fmt.Println(ChangeBase(8, 2))
    fmt.Println(ChangeBase(7, 2))
}
```

This code works by repeatedly dividing the input number by the base and appending the remainder to a slice. It then reverses the slice and joins the elements into a single string.

This will give the desired output:

```
22
1000
111
```

I hope this helps.

A: The issue with your code is that you are appending the result to the front of the string, while you should be appending it to the end. In other words, you should be doing the reverse of what you're doing. 

Here's the corrected code: