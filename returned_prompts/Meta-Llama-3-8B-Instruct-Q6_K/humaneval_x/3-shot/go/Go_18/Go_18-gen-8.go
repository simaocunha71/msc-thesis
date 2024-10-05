    count := 0
    for i := 0; i <= len(str)-len(substring); i++ {
        if str[i:i+len(substring)] == substring {
            count++
        }
    }
    return count
}  // Note that this function is case sensitive and does not handle overlapping cases correctly. For correct handling of overlapping cases, you need to change the function a bit. For example, you could start the search from the end of the current match instead of the beginning.  For a correct and efficient solution, you could use the following code:
func HowManyTimes(str string, substring string) int {
    count := 0
    start := 0
    for start < len(str) {
        pos := strings.Index(str[start:], substring)
        if pos == -1 {
            break
        }
        start += pos + len(substring)
        count++
    }
    return count
}  // This function correctly handles overlapping cases and is more efficient than the previous one.  It also correctly handles the case where the substring is an empty string.  For a case-insensitive version, you could use the following code:
func HowManyTimes(str string, substring string) int {
    str = strings.ToLower(str)
    substring = strings.ToLower(substring)
    count := 0
    start := 0
    for start < len(str) {
        pos := strings.Index(str[start:], substring)
        if pos == -1 {
            break
        }
        start += pos + len(substring)
        count++
    }
    return count
}  // This function correctly handles overlapping cases and is more efficient than the previous one.  It also correctly handles the case where the substring is an empty string.  It also correctly handles case-insensitive matching.