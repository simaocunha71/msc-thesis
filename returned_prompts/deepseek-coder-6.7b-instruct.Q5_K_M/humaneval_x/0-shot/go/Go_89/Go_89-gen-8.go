    result := ""
    for _, c := range s {
        switch {
        case 'a' <= c && c <= 'z':
            result += string((c-'a'+2*2+26)%26 + 'a')
        case 'A' <= c && c <=