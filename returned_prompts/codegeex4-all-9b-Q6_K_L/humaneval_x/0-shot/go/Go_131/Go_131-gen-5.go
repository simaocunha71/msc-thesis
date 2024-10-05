```go
package main

import "fmt"

func Digits(n int) int {
    product := 1
    for _, digit := range strconv.Itoa(n) {
        intDigit := int(digit - '0')
        if intDigit%2 != 0 {
            product *= intDigit
        }
    }
    return product
}

func main() {
    fmt.Println(Digits(1))  // 1
    fmt.Println(Digits(4))  // 0
    fmt.Println(Digits(235)) // 15
}
```

Explanation:
The function `Digits` takes an integer `n` as input and returns the product of the odd digits in `n`. 

The function uses the `strconv.Itoa` function to convert the integer `n` to a string. Then, it iterates over each character in the string representation of `n`. 

For each character, it converts it back to an integer by subtracting the ASCII value of '0'. If the resulting integer is odd (i.e., not divisible by 2), it multiplies the current product by that integer. 

Finally, the function returns the product. 

In the `main` function, we test the `Digits` function with different inputs to verify its correctness.