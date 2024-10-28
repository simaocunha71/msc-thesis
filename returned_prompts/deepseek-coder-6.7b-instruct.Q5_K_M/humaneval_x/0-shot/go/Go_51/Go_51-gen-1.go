    re := regexp.MustCompile("[aeiouAEIOU]")
    text = re.ReplaceAllString(text, "")
    return text
}

