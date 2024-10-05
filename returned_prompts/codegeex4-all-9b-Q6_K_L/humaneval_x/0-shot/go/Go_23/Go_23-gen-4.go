func Strlen(str string) int {
    return len(str)
}

The len() function in Go returns the number of bytes in a string, not the number of characters. If you want to get the number of characters, you can use utf8.RuneCountInString(str) instead.

func Strlen(str string) int {
    return utf8.RuneCountInString(str)
}
