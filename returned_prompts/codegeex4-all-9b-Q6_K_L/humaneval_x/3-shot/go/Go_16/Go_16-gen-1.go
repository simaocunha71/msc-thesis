
for _, c := range str {
        if strings.ContainsRune(str, c){
            count += 1
        }
    }

should be
for _, c := range str {
        if strings.IndexRune(str, c) == -1 {
            count += 1
        }
    }

since strings.ContainsRune will return true for every character in the string, so every character will be counted. You should check if the rune is not in the string, not if it is.