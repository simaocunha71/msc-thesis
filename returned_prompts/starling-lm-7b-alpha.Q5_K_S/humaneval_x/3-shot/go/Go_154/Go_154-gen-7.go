    for _, c := range b {
        index := strings.Index(a,string(c))
        if index != -1 {
            return true
        }

        a = a[index+1:] + a[:index]
    }
    return false
}



