    for i := 0; i < len(b); i++ {
        if strings.Contains(a,b[:i+1]){
            return true
        }
    }
    return false
}



