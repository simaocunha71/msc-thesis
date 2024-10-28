To convert a decimal number to binary, you can use the following steps:

1. Initialize an empty string, `binary`, to store the binary representation.
2. Use a loop to divide the decimal number by 2 until it becomes 0.
3. For each division, check the remainder. If the remainder is 0, append '0' to the `binary` string. If the remainder is 1, append '1' to the `binary` string.
4. Reverse the `binary` string to get the correct order of binary digits.
5. Return the `binary` string with the extra characters 'db' at the beginning and at the end.

Here's the updated code:

```go
func DecimalToBinary(decimal int) string {
	binary := ""

	for decimal > 0 {
		remainder := decimal % 2
		if remainder == 0 {
			binary += "0"
		} else {
			binary += "1"
		}
		decimal = decimal / 2
	}

	// Reverse the binary string
	reversedBinary := ""
	for i := len(binary) - 1; i >= 0; i-- {
		reversedBinary += string(binary[i])
	}

	return "db" + reversedBinary + "db"
}
```

Now, let's test the function with the given examples:

```go
func main() {
	fmt.Println(DecimalToBinary(15))   // Output: "db1111db"
	fmt.Println(DecimalToBinary(32))   // Output: "db100000db"
}
```

The output should be:

```
db1111db
db100000db
```