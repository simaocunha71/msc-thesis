    parts := strings.SplitN(s, " ", 2)
    timestamp := parts[0]
    encodedString := parts[1]
    decodedString := DecodeCyclic(encodedString)
    return decodedString, timestamp

}

