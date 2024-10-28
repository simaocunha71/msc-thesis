    result := extensions[0]
    cap_count := 0
    sm_count := 0
    for _, c := range extensions[0] {
        if c >= 'A' && c <= 'Z' {
            cap_count += 1
        }else if c >= 'a' && c <= 'z' {
            sm_count += 1
        }
    }
    strength := float64(cap_count) - float64(sm_count)
    for _, extension := range extensions {
        cap_count = 0
        sm_count = 0
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                cap_count += 1
            }else if c >= 'a' && c <= 'z' {
                sm_count += 1
            }
        }
        new_strength := float64(cap_count) - float64(sm_count)
        if new_strength > strength {
            result = extension
            strength = new_strength
        }
    }
    return class_name + "." + result
}



