    for _, c := range s {
        if c >= 'A' && c <= 'Z' {
            cap_count += 1
        } else if c >= 'a' && c <= 'z' {
            sm_count += 1
        }
    }

    return float64(cap_count) - float64(sm_count)
}



