    pattern := `[^aeiouAEIOU]`
    return regexp.MustCompile(pattern).ReplaceAllString(text, "")
}



