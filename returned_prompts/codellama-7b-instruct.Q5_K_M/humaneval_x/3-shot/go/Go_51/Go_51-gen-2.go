    var vowels = "aeiou"
    var pattern = "[^"+vowels+"]+"
    var re = regexp.MustCompile(pattern)
    return re.ReplaceAllString(text, "")
}



