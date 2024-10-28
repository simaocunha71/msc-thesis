    if len(s) < 3{
        return false
    }

    for i := 0; i < len(s)-2; i++ {
        if s[i:i+3] == s[i+1:i+4]{
            return false
        }
    }
    return true
}



