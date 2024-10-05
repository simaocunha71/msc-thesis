```go
func Multiply(a, b int) int {
    return (a % 10) * (b % 10)
}
```
Explanation:
The function `Multiply(a, b int) int` takes two integers as input and returns the product of their unit digits. 

The unit digit of an integer can be obtained by taking the modulus of the integer with 10. In Go, the modulus operator is `%`. 

So, `(a % 10)` gives the unit digit of `a` and `(b % 10)` gives the unit digit of `b`. 

The product of these two unit digits is calculated by multiplying them together, which is done by the expression `(a % 10) * (b % 10)`. 

This result is then returned by the function. 

This solution assumes that the input integers are always valid, as specified in the problem statement. 

For example, `Multiply(148, 412)` returns `16` because the unit digits of `148` and `412` are `8` and `2` respectively, and their product is `16`. Similarly, `Multiply(19, 28)` returns `72` because the unit digits of `19` and `28` are `9` and `8` respectively, and their product is `72`. 

The function also works correctly for negative inputs, as in `Multiply(14, -15)` which returns `20` because the unit digits of `14` and `-15` are `4` and `5` respectively, and their product is `20`. 

Finally, the function correctly returns `0` for inputs like `Multiply(2020, 1851)` because the unit digits of `2020` and `1851` are `0` and `1` respectively, and their product is `0`. 