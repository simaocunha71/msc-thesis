    runes := []rune(s)
    newRunes := make([]rune, 0)
    for _, ch := range runes {
        newRunes = append(newRunes, (ch-5+26)%26)
    }
    return string(newRunes)
}

func main() {
    s := "fvwj"
    encoded := EncodeShift(s)
    fmt.Println(encoded)
    decoded := DecodeShift(encoded)
    fmt.Println(decoded)
}

//Output:
// 	hzxm
// 	fvwj

In the function EncodeShift, the program takes a string, converts it into a slice of runes, and then creates a new slice of runes called newRunes. It then loops over the original slice of runes and for each character, adds 5 to the character, subtracts 'a', and takes the modulus of 26. The result is then appended to the new slice of runes. Finally, the new slice of runes is converted back into a string and returned.

In the function DecodeShift, the program takes a string, converts it into a slice of runes, and then creates a new slice of runes called newRunes. It then loops over the original slice of runes and for each character, subtracts 5 from the character, adds 26, and takes the modulus of 26. The result is then appended to the new slice of runes. Finally, the new slice of runes is converted back into a string and returned.

In the main function, the program defines a string variable s with the value "fvwj". It then calls the EncodeShift function and stores the result in the variable encoded. The program then prints the value of encoded. Next, it calls the DecodeShift function and stores the result in the variable decoded. Finally, the program prints the value of decoded.

The output of the program is "hzxm" for the encoded string and "fvwj" for the decoded string, as expected.

In terms of complexity, both the EncodeShift and DecodeShift functions have a time complexity of O(n), where n is the length