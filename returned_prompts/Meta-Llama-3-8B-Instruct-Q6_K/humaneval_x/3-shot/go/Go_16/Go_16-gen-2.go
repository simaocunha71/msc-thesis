    str = strings.ToLower(str)
    charSet := make(map[rune]bool)
    for _, value := range str {
        charSet[value] = true
    }
    return len(charSet)
}  // O(n) where n is the length of the string. This is because we're doing a single pass through the string.  The space complexity is also O(n) as in the worst case scenario the map will hold all the characters in the string.