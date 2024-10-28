    if strings.Contains(txt," ") || strings.Contains(txt,",") {
        return strings.Fields(txt)
    }else {
        odd_chars := 0
        for _, c := range txt {
            if c >= 'a' && c <= 'z' && (c-'a') % 2 == 1 {
                odd_chars += 1
            }
        }
        return odd_chars
    }
}



