    if strings.ContainsAny(txt," ") {
        return strings.Split(txt," ")
    }else if strings.ContainsAny(txt,",") {
        return strings.Split(txt,",")
    }else{
        count := 0
        for i := 0; i < len(txt); i++ {
            if i % 2 == 1 {
                count++
            }
        }
        return count
    }
}



