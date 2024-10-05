    byte_s := []byte(s)

    for i, c := range byte_s {
        if 'a' <= c && c <= 'z' || 'A' <= c && c <= 'Z' {
            if 'a' <= c && c <= 'z' {
                byte_s[i] = c - 32
            } else {
                byte_s[i] = c + 32
            }
        }
    }

    return string(byte_s)
}



