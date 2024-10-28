    if strings.Contains(txt," ") {
        return strings.Split(txt," ")
    }else if strings.Contains(txt, ",") {
        return strings.Split(txt,",")
    }else{
        return len([]rune(txt)) - len(strings.ToUpper(txt))
    }
}



