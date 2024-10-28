    re := regexp.MustCompile(`[aeiouAEIOU]`)
    return re.ReplaceAllString(text, "")
}