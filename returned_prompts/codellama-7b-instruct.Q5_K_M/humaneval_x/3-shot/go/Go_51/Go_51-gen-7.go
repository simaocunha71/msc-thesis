    var vowels = []string{"a", "e", "i", "o", "u"}
    var pattern string = "[^a-zA-Z]"
    var re *regexp.Regexp
    for _, v := range vowels {
        pattern += "|[^"+v+"]"
    }

    re = regexp.MustCompile(pattern)
    return re.ReplaceAllString(text, "")
}



