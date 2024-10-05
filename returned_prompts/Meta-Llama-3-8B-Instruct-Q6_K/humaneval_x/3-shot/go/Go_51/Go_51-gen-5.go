    vowels := regexp.MustCompile(`[aeiouAEIOU]`)
    return vowels.ReplaceAllString(text, "")
}

