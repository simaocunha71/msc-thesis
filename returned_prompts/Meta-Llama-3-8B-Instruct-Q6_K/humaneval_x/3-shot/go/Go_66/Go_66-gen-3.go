    sum := 0
    for _, c := range x {
        if c >= 'A' && c <= 'Z' {
            sum += int(c - 'A' + 65)
        }
    }
    return sum
}  // ASCII code for 'A' is 65, 'B' is 66, 'C' is 67, and so on. So subtract the ASCII value of 'A' from the character to get the value of the alphabet. Then add 65 to get the ASCII code of the character.  // ASCII code for 'a' is 97, 'b' is 98, 'c' is 99, and so on. So subtract the ASCII value of 'a' from the character to get the value of the alphabet. Then add 97 to get the ASCII code of the character.  // ASCII code for '0' is 48, '1' is 49, '2' is 50, and so on. So subtract the ASCII value of '0' from the character to get the value of the digit. Then add 48 to get the ASCII code of the character.