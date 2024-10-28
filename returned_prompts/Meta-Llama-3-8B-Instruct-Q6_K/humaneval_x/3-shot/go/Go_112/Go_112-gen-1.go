    filtered := strings.Map(func(r rune) rune {
        for _, c := range c {
            if r == c {
                return -1
            }
        }
        return r
    }, s)
    result := strings.ToLower(string(filtered))
    return [2]interface{}{result, result == strings.Reverse(result)}
}