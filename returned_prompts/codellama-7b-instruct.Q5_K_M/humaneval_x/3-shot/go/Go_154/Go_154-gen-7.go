    for i := 0; i < len(b); i++ {
        var cyc_b string
        for j := 0; j < len(b); j++ {
            cyc_b = cyc_b + string(b[j])
        }
        if strings.Contains(cyc_b, b[i:]) {
            return true
        }
    }
    return false
}



