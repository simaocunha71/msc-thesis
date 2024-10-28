    for i := 0; i < len(a); i++ {
        if strings.Contains(a,b){
            return true
        }
        b = string(b[1:]+b[:1])
    }
    return false
}



