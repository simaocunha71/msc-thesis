Here is the solution:
```go
func DecimalToBinary(decimal int) string {
    binary := ""
    for decimal > 0 {
        remainder := decimal % 2
        if remainder == 1 {
            binary = "1" + binary
        } else {
            binary = "0" + binary
        }
        decimal = decimal / 2
    }
    return "db" + binary + "db"
}
```
Explanation:
The function `DecimalToBinary` takes an integer `decimal` as input and returns a string representing the binary form of the decimal number.

The function initializes an empty string `binary` to store the binary representation of the decimal number.

It then enters a loop that continues until the `decimal` number becomes 0.

In each iteration of the loop, it calculates the remainder of the `decimal` number when divided by 2 using the modulus operator `%`. If the remainder is 1, it appends the string "1" to the `binary` string; otherwise, it appends the string "0".

After calculating the remainder, it updates the `decimal` number by performing integer division by 2 using the `/` operator.

Once the `decimal` number becomes 0, the loop terminates, and the function returns the `binary` string concatenated with the extra characters "db" at the beginning and end.

For example, if the input is `15`, the function will calculate the binary representation as "1111" and return the string "db1111db". Similarly, if the input is `32`, the function will calculate the binary representation as "100000" and return the string "db100000db".