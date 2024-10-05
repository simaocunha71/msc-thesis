    if strings.Contains(txt," ") {
        return strings.Split(txt," ")
    }
    if strings.Contains(txt,",") {
        return strings.Split(txt,",")
    }
    count := 0
    for i, c := range txt {
        if i%2 == 0 && c >= 'a' && c <= 'z' {
            count += 1
        }
    }
    return count
}



