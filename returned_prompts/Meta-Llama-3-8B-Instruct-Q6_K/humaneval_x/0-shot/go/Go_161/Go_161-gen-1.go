    result := ""
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result += string(c + 'A' - 'a')
        } else if c >= 'A' && c <= 'Z' {
            result += string(c - 'A' + 'a')
        } else {
            result += string(c)
        }
    }
    if result == s {
        return reverse(s)
    }
    return result
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func main() {
    fmt.Println(Solve("1234")) // Output: "4321"
    fmt.Println(Solve("ab"))   // Output: "AB"
    fmt.Println(Solve("#a@C")) // Output: "#A@c"
}