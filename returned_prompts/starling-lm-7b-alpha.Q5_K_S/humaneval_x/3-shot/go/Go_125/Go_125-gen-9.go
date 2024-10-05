    if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    }
    count:=0
    for _, c := range txt {
        if c >= 'a' && c <= 'z' {
            if c % 2 != 0 {
                count++
            }
        }
    }
    return count
}



