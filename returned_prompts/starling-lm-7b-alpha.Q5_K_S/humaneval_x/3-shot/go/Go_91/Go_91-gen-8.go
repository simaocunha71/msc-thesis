    regexp := regexp.MustCompile(`I.*[?.!]`)
    return regexp.FindStringIndex(S)[0]
}



