func CircularShift(x int, shift int) string {
    // Convert the integer to a string
    s := strconv.Itoa(x)

    // If the shift is greater than the length of the string, return the reversed string
    if shift > len(s) {
        return reverse(s)
    }

    // Shift the digits right by shift
    s = s[shift:] + s[:shift]

    return s
}

func reverse(s string) string {
    // Convert the string to a slice of runes
    runes := []rune(s)

    // Reverse the slice of runes
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }

    // Convert the slice of runes back to a string
    return string(runes)
}
