    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    }else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    }

    count := 0
    for i := 0; i < len(txt); i++ {
        if txt[i] >= 'a' && txt[i] <= 'z' {
            count += 1
        }
    }
    return count
}



