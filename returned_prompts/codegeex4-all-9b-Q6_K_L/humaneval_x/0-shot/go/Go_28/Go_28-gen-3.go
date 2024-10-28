func Concatenate(strings []string) string {
    result := ""
    for _, s := range strings {
        result += s
    }
    return result
}