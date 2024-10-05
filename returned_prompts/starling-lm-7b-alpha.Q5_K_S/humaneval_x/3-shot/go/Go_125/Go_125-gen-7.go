    if strings.Contains(txt," ") || strings.Contains(txt,","){
        return strings.Fields(txt)
    }
    count := 0
    for _,r := range txt {
        if r >= 'a' && r <= 'z' {
            if r % 2 != 0 {
                count += 1
            }
        }
    }
    return count
}




