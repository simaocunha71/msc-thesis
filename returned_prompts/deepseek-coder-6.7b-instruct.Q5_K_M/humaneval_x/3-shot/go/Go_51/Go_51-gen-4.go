    re := regexp.MustCompile("(a|e|i|o|u|A|E|I|O|U)")
    return re.ReplaceAllString(text, "")
}



