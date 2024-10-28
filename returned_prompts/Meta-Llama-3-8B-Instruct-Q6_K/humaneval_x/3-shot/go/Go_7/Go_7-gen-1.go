    return strings.FilterFunc(stringList, func(s string) bool {
        return strings.Contains(s, substring)
    })
}