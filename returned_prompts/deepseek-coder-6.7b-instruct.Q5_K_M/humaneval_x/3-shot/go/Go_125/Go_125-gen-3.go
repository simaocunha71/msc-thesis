    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    } else {
        count := 0
        for _, c := range txt {
            if 'a' <= c && c <= 'z' && int(c-'a')%2 == 1 {
                count++
            }
        }
        return count
    }
}



