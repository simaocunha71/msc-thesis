    for i:=0; i< len(s); i+=3{
        if i+2 < len(s) && s[i] == s[i+1] || s[i+1] == s[i+2] || s[i] == s[i+2]{
            return false
        }
    }
    return true
}



