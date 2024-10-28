    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    }
    if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    }
    count := 0
    for _, c := range txt {
        if 'a' <= c && c <= 'z' {
            if int(c-'a')%2 == 1 {
                count++
            }
        }
    }
    return count
}



