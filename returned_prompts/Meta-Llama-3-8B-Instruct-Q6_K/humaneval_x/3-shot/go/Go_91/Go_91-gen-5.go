    re, _ := regexp.Compile(`^[Ii].*[\.\?\!]`)
    return len(re.FindAllString(S, -1))
} 



