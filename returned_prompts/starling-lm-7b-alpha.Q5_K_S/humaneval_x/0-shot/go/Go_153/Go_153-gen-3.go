    var cap, sm, strength int
    var strongestExtension string
    for _, ext := range extensions {
        cap = 0
        sm = 0
        for _, r := range ext {
            if 'A' <= r && r <= 'Z' {
                cap++
            } else if 'a' <= r && r <= 'z' {
                sm++
            }
        }
        strength = cap - sm
        if strength > 0 && (strength > strengthOfStrongestExtension || strongestExtension == "") {
            strengthOfStrongestExtension = strength
            strongestExtension = ext
        }
    }
    return class_name + "." + strongestExtension
}




func StrongestExtension(class_name string, extensions []string) string {
    strengthOfStrongestExtension := -math.MaxInt64
    strongestExtension := ""
    for _, ext := range extensions {
        cap, sm := 0, 0
        for _, r := range ext {
            if 'A' <= r && r <= 'Z' {
                cap++
            } else if 'a' <= r && r <= 'z' {
                sm++
            }
        }
        strength := cap - sm
        if strength > 0 && (strength > strengthOfStrongestExtension || strongestExtension == "") {
            strengthOfStrongestExtension = strength
            strongestExtension = ext
        }
    }
    return class_name + "." + strongestExtension
}




func StrongestExtension(class_name string, extensions []string) string {
    strengthOfStrongestExtension := -math.MaxInt64
    strongestExtension := ""
    for _, ext := range extensions {
        cap, sm := 0, 0
        for _, r := range ext {
            if 'A' <= r && r <= 'Z' {
                cap++
            } else if 'a' <= r && r <= 'z' {
                sm++
            }
        }
        strength := cap - sm
        if strength > 0 && (strength > strengthOfStrongestExtension || strongestExtension == "") {
            strengthOfStrongestExtension = strength
            strongestExtension =