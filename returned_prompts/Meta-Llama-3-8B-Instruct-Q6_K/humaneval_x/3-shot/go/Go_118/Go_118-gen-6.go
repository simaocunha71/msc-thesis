    bytesWord := []byte(word)
    for i := len(bytesWord) - 1; i >= 0; i-- {
        if "AEIOUaeiou"[0] <= byte(bytesWord[i]) && byte(bytesWord[i]) <= "AEIOUaeiou"[4] {
            if i < len(bytesWord) - 1 && "AEIOUaeiou"[0] > byte(bytesWord[i+1]) && byte(bytesWord[i+1]) > "AEIOUaeiou"[4] {
                return string(bytesWord[i])
            }
        }
    }
    return ""
}