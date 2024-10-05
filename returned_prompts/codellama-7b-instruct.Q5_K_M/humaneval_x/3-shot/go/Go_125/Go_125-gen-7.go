    if strings.Contains(txt," ") {
        return strings.Split(txt," ")
    }else if strings.Contains(txt,",") {
        return strings.Split(txt,",")
    }else {
        count := 0
        for i := 0; i < len(txt); i++ {
            if txt[i] < 'a' || txt[i] > 'z' {
                continue
            }
            if i%2==1 {
                count +=1
            }
        }
        return count
    }
}



