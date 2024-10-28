    result := 0
    r := regexp.MustCompile(`I.*[?.!]`)
    if r.MatchString(S) {
        result += 1
    }
    return result
}



