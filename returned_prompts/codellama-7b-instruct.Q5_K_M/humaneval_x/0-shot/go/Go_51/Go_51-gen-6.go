    r, _ := regexp.Compile(`[aeiou]`)
    return r.ReplaceAllString(text, "")
}

