    re := regexp.MustCompile(`[aeiou]+`)
    return re.ReplaceAllString(text, "")
}



