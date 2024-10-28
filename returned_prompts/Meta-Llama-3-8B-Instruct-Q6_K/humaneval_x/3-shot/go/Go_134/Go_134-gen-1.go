    lastChar := strings.ToLower(txt[strings.LastIndex(txt, " ")+1:])
    return len(lastChar) == 1 && ("a" <= lastChar[0] && lastChar[0] <= "z")
}