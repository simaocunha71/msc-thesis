    if len(l) == 0{
        return true
    }
    var direction int = l[1] - l[0]

    for i := 1; i < len(l); i++ {
        if l[i] - l[i-1] != direction {
            return false
        }
    }
    return true
}



