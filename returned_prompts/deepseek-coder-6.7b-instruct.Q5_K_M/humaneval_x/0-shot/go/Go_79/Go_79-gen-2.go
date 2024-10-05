	binary := ""
	for decimal > 0 {
		remainder := decimal % 2
		binary = fmt.Sprintf("%d%s", remainder, binary)
		decimal = decimal / 2
	}
	return "db" + binary + "db"
}

func main() {
	fmt.Println(DecimalToBinary(15))
	fmt.Println(DecimalToBinary(32))
}

// You can run this code in your local environment to check the output
```

This Go code converts a decimal number to a binary number by taking the remainder of the division by 2 and concatenating it to the front of the binary string. This process is repeated until the decimal number is 0. At the end, it adds the extra 'db' characters at the beginning and end of the string.

For example, for the input 15, the binary representation is 1111, so the output is "db1111db". For the input 32, the binary representation is 100000, so the output is "db100000db".

This function can be used in any program that needs to convert decimal numbers to binary.

Note: This function assumes that the input will be a positive integer. If negative numbers or non-integer inputs are expected, additional error checking should be added.


## Python Solution:

```python
# Python program to convert Decimal number to Binary number

def DecimalToBinary(decimal):
    binary = bin(decimal).replace("0b", "")
    return "db" + binary + "db"

print(DecimalToBinary(15))  # returns "db1111db"
print(DecimalToBinary(32))  # returns "db100000db"
```

This Python code uses the built-in function `bin()` to convert the decimal number to binary. The `replace()` method is used to remove the "0b" prefix that `bin()` adds to the binary string. The `db` characters are added at the beginning and end of the binary string.

This function can be used in any program that needs to convert decimal numbers to binary.

