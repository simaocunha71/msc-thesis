    if strings.Contains(txt, " ") || strings.Contains(txt, ","){
        return strings.Fields(txt)
    }
    result := 0
    for _, c := range txt {
        if c >= 'a' && c <= 'z' {
            if (ord(c) % 2) == 1 {
                result += 1
            }
        }
    }
    return result
}



