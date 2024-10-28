The unit digits of the input integers are the last digits. To find the product of these unit digits, you can simply multiply them together. Here's how you can do it in Go:

```go
func Multiply(a, b int) int {
    return int(math.Abs(float64(a%10)) * math.Abs(float64(b%10)))
}
```

This function uses the modulo operator (`%`) to get the last digit of each input integer. It then uses the `math.Abs` function to ensure that the digits are always positive, as the absolute value of a number is always positive. The result is the product of these unit digits. 

For example, if you call `Multiply(148, 412)`, it will return `16` (which is the product of `8` and `2`, the last digits of `148` and `412` respectively). Similarly, if you call `Multiply(19, 28)`, it will return `72` (which is the product of `9` and `8`, the last digits of `19` and `28` respectively). 

This function also works correctly for negative inputs, as the `math.Abs` function takes care of handling the signs. For example, if you call `Multiply(14, -15)`, it will return `20` (which is the product of `4` and `5`, the absolute values of the last digits of `14` and `-15` respectively). 

This function assumes that the input is always valid, as specified in the problem statement. If the input can be invalid, you should add error checking code to handle invalid inputs. 