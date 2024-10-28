    var count int
    for _, v := range nums {
        if v > 10 {
            str := strconv.Itoa(v)
            firstChar := str[0]
            lastChar := str[len(str)-1]
            if firstChar != '1' && firstChar != '3' && firstChar != '5' &&
                firstChar != '7' && firstChar != '9' &&
                lastChar != '1' && lastChar != '3' && lastChar != '5' &&
                lastChar != '7' && lastChar != '9' {
                count++
            }
        }
    }
    return count
}

Here is my solution, but the result is incorrect.

I tried to use the "strconv.Itoa" to convert the number to a string, and then use "str[0]" and "str[len(str)-1]" to get the first and last digits of the number.

However, the result is incorrect.

It seems that I have not correctly converted the number to a string and obtained the first and last digits.

What is the correct way to convert the number to a string and obtain the first and last digits of the number?

In addition, is there a faster way to write the above code?

Here is my incorrect solution:

```go
package main

import (
    "fmt"
    "strconv"
)

func Specialfilter(nums []int) int {
    var count int
    for _, v := range nums {
        if v > 10 {
            str := strconv.Itoa(v)
            firstChar := str[0]
            lastChar := str[len(str)-1]
            if firstChar != '1' && firstChar != '3' && firstChar != '5' &&
                firstChar != '7' && firstChar != '9' &&
                lastChar != '1' && lastChar != '3' && lastChar != '5' &&
                lastChar != '7' && lastChar != '9' {
                count++
            }
        }
    }
    return count
}

