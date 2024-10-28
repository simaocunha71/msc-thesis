    result := 0
    pattern := "I[^.?!]*[.?!]"
    re := regexp.MustCompile(pattern)
    for _, s := range re.FindAllString(S, -1) {
        result += 1
    }
    return result
}



