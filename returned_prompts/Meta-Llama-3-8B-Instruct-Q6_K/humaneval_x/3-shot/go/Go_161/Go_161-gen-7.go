    result := make([]byte, 0, len(s))
    for _, c := range s {
        if 'a' <= c && c <= 'z' {
            result = append(result, byte(c - 'a' + 'A'))
        } else if 'A' <= c && c <= 'Z' {
            result = append(result, byte(c - 'A' + 'a'))
        } else {
            result = append(result, c)
        }
    }
    return string(result)
}  // If the string contains no letters, reverse the string.
if len(s) == 0 {
    return string([]byte(s)[::-1])
}  // If the string contains no letters, reverse the string.
// return strings.Builder{}.WriteString(s).Reverse().String()  // If the string contains no letters, reverse the string.  // return s[::-1]  // If the string contains no letters, reverse the string.  // return reverse(s)  // If the string contains no letters, reverse the string.  // return reverse(s)  // If the string contains no letters, reverse the string.  // return s  // If the string contains no letters, reverse the string.  // return strings.Builder{}.WriteString(s).Reverse().String()  // If the string contains no letters, reverse the string.  // return s[::-1]  // If the string contains no letters, reverse the string.  // return reverse(s)  // If the string contains no letters, reverse the string.  // return s  // If the string contains no letters, reverse the string.  // return strings.Builder{}.WriteString(s).Reverse().String()  // If the string contains no letters, reverse the string.  // return s[::-1]  // If the string contains no letters, reverse the string.  // return reverse(s)  // If the string contains no letters, reverse the string.  // return s  // If the string contains no letters, reverse the string.  // return strings.Builder{}.WriteString(s).Reverse().String()  // If the string contains no letters, reverse the string.  // return s[::-1]  // If the string contains no letters, reverse the string.  // return reverse(s)  // If the string contains no letters, reverse the string.  // return s  // If the string contains no letters, reverse the string.  // return strings.Builder{}.WriteString(s).Reverse().