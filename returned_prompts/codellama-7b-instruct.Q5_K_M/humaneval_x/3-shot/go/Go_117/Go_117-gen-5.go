    result := make([]string, 0)
    s = strings.ToLower(s)
    s = strings.ReplaceAll(s, " ", "")

    for _, word := range strings.Split(s, ""){
        if strings.Count(word, "a")+strings.Count(word, "e")+strings.Count(word, "i")+strings.Count(word, "o")+strings.Count(word, "u")+strings.Count(word, "y") == n{
            result = append(result, word)
        }
    }
    return result
}



