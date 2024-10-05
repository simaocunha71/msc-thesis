    var result string
    for _, s := range strings {
        result += s
    }
    return result
}

// This is also possible with strings.Join()
func Concatenate(strings []string) string {
    return strings.Join(strings, "")
}