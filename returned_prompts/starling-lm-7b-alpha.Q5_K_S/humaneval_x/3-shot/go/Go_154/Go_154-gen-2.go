    for _, c := range b {
        if a.Index(string(c)) >= 0 {
            return true
        }
    }
    return CycpatternCheck(a, b[1:]+string(b[0]))
}



