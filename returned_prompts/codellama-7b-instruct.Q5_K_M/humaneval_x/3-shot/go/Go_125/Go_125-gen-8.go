    if strings.Contains(txt, " ") {
        return strings.Fields(txt)
    }
    if strings.Contains(txt, ",") {
        return strings.Fields(txt)
    }
    count := 0
    for i := 0; i < len(txt); i++ {
        if (txt[i] >= 'a' && txt[i] <= 'z') || (txt[i] >= 'A' && txt[i] <= 'Z') {
            count++
        }
    }
    return count % 2
}



