	var result []byte
	for decimal > 0 {
		result = append(result, byte(decimal&1)+'0')
		decimal >>= 1
	}
	return "db" + string(result) + "db"
}

// To convert a number from base 10 to base 2 (binary), you need to repeatedly divide the
// number by 2 and keep track of the remainders.
// The remainders will be the least significant bits of the binary number.

// For example, to convert the decimal number 15 to binary, you perform the following
// steps:
// 
// 15 / 2 = 7 remainder 1 -> 1 is the least significant bit.
// 7 / 2 = 3 remainder 1 -> 1 is the next least significant bit.
// 3 / 2 = 1 remainder 1 -> 1 is the next least significant bit.
// 1 / 2 = 0 remainder 1 -> 1 is the next least significant bit.
// 0 / 2 = 0 remainder 1 -> 1 is the least significant bit.
// 
// When you have finished, you read the remainders in reverse order to get the binary
// representation of the number: 1111.

// The binary representation of a number is a sequence of 0s and 1s. It is a base 2
// representation of the number.

// Here are some binary numbers for reference:
// 
// 0000 = 0
// 0001 = 1
// 0010 = 2
// 0011 = 3
// 0100 = 4
// 0101 = 5
// 0110 = 6
// 0111 = 7
// 1000 = 8
// 1001 = 9
// 1010 = 10
// 1011 = 11
// 1100 = 12
// 1101 = 13
// 1110 = 14
// 1111 = 15

// Note that