    sum := 0
    for _, c := range x {
        if c >='A' && c <= 'Z' {
            sum += int(c - 'A' + 65)
        }
    }
    return sum
}  // ASCII code for 'A' is 65, for 'B' is 66, etc. So subtract 'A' from the character and add 65 to get the ASCII code.