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
Here's an explanation of the code:

* We initialize an empty string `binary` to store the binary representation of the decimal number.
* We loop until the decimal number becomes 0.
* In each iteration, we calculate the remainder of the decimal number when divided by 2 using the modulo operator `%`. This gives us the least significant bit (LSB) of the binary representation.
* If the remainder is 1, we append a '1' to the `binary` string; otherwise, we append a '0'.
* We then update the decimal number by integer dividing it by 2.
* After the loop, we return the `binary` string with the extra 'db' characters added at the beginning and end.

You can test this function with the examples you provided:
```go
fmt.Println(DecimalToBinary(15))  // Output: db1111db
fmt.Println(DecimalToBinary(32))  // Output: db100000db
```A: Here is the solution:
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
Here's an explanation of the code:

* We initialize an empty string `binary` to store the binary representation of the decimal number.
* We loop until the decimal number becomes 0.
* In each iteration, we calculate the remainder of the decimal number when divided by 2 using the modulo operator `%`. This gives us the least significant bit (LSB) of the binary representation.
* If the remainder is 1, we append a '1' to the `binary` string; otherwise, we append a '0'.
* We then update the decimal number by integer dividing it by 2.
* After the loop, we return