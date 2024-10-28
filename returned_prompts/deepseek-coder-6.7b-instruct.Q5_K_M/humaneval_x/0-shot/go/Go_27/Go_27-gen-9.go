    var flipped string
    for _, letter := range str {
        if unicode.IsLower(letter) {
            flipped += strings.ToUpper(string(letter))
        } else if unicode.IsUpper(letter) {
            flipped += strings.ToLower(string(letter))
        } else {
            flipped += string(letter)
        }
    }

    return flipped
}

func main() {
    fmt.Println(FlipCase("Hello")) // 'hELLO'
}

