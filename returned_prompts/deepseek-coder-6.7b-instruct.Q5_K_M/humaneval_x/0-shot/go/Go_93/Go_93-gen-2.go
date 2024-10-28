    encoded := ""

B:
    for _, char := range message {
        c := string(char)

        switch strings.ToLower(c) {
        case "a":
            encoded += "C"
        case "e":
            encoded += "G"
        case "i":
            encoded += "K"
        case "o":
            encoded += "Q"
        case "u":
            encoded += "W"
        default:
            switch c {
            case strings.ToUpper(c):
                encoded += strings.ToLower(c)
            case strings.ToLower(c):
                encoded += strings.ToUpper(c)
            }
        }
    }

C:
    return encoded
}

// Test cases
func main() {
    fmt.Println(Encode("test")) // Expected: 'TGST'
    fmt.Println(Encode("This is a message")) // Expected: 'tHKS KS C MGSSCGG'
}

