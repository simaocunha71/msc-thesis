
// Convert the integer to a string.
s := strconv.Itoa(x)

B:

// Reverse the string.
reverse := Reverse(s)

C:

// If shift is greater than number of digits, return the reversed string.
// Otherwise, return the first (shift) characters of the reversed string.
if shift > len(reverse) {
    return reverse
}
return reverse[:shift]
}

func Reverse(s string) string {
// Create a new string with the characters in reverse order.
// Create a new string with the characters in reverse order.
runes := []rune(s)
for i, j := 0, len(runes)-1; i < len(runes)/2; i, j = i+1, j-1 {
    runes[i], runes[j] = runes[j], runes[i]
}
return string(runes)
}
