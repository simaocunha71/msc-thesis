    decrypted := ""

B:
    for _, c := range s {
        if unicode.IsLetter(c) {
            if unicode.IsUpper(c) {
                decrypted += string((c-'A'-2