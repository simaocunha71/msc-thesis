    if len(b) > len(a){
        return false
    }
    for i := 0; i < len(a); i++ {
        if strings.Contains(a[i:],b) {
            return true
        }
    }
    return false
}



