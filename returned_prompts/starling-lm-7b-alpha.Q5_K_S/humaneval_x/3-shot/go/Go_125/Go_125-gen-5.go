    if strings.Contains(txt," ") {
        return strings.Split(txt," ")
    }else if strings.Contains(txt,",") {
        return strings.Split(txt,",")
    }else {
        counter := 0
        for _, c := range txt {
            if c >= 'a' && c <= 'z' {
                if (c % 2 == 1) {
                    counter += 1
                }
            }
        }
        return counter
    }
}



