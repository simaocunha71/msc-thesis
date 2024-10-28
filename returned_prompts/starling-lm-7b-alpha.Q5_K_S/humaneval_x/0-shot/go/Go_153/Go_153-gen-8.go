    min := math.Inf(-1)
    name := ""
    for _, name = range extensions {
        cap := 0
        sm := 0
        for _, c := range name {
            if 'A' <= c && c <= 'Z' {
                cap++
            } else {
                sm++
            }
        }
        strength := float64(cap) - float64(sm)
        if strength < min {
            min = strength
            name = name
        }
    }
    return class_name + "." + name
}






func StrongestExtension(class_name string, extensions []string) string {
    min := math.Inf(-1)
    name := ""
    for _, name = range extensions {
        cap := 0
        sm := 0
        for _, c := range name {
            if 'A' <= c && c <= 'Z' {
                cap++
            } else {
                sm++
            }
        }
        strength := float64(cap) - float64(sm)
        if strength == min {
            name = name
        } else if strength < min {
            min = strength
            name = name
        }
    }
    return class_name + "." + name
}















































































































































































































