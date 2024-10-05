    shift := 2*2
    runes := []rune(s)

    for i := 0; i < len(runes); i++ {
        if 'a' <= runes[i] && runes[i] <= 'z' {
            runes[i] = 'a' + (runes[i]-'a'+rune(shift))%26
        } else if 'A' <= runes[i] && runes[i] <= 'Z' {
            runes[i] = 'A' + (runes[i]-'A'+rune(shift))%26
        }
    }

    return string(runes)
}



