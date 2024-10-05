    if len(txt) > 0{
        last_char := txt[len(txt)-1]
        if !strings.ContainsAny(string(last_char), "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
            return false
        }else{
            return !strings.HasSuffix(txt, " ")
        }
    }else{
        return false
    }

}

