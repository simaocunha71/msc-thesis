    var alphabet = []string{"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}
    var encrypted_string = ""
    for _, c := range s {
        index := strings.Index(strings.Join(alphabet, ""), string(c))
        if index+2 < len(alphabet) {
            encrypted_string += alphabet[index+2*2]
        } else {
            encrypted_string += alphabet[(index+2*2)-len(alphabet)]
        }
    }
    return encrypted_string
}



