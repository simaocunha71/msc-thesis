    alphabet := "abcdefghijklmnopqrstuvwxyz"
    encrypted := make([]byte, len(s))
    for i, c := range s {
        idx := strings.IndexByte(alphabet, byte(c))
        if idx == -1 {
            encrypted[i] = byte(c)
        } else {
            new_idx := (idx + 4*2) % 26
            encrypted[i] = alphabet[new_idx]
        }
    }
    return string(encrypted)
}  // 4*2 means 8 places. You can also use (idx + 8) % 26 for the same effect.