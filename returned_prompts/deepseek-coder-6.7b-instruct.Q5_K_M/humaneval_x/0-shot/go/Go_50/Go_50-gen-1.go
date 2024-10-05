// returns decoded string by shifting every character by 5 in the alphabet.
func DecodeShift(s string) string  {
    runes  := []rune(s)
    newRunes  := make([]rune, 0)
    for  _, ch := range runes  {
        newRunes = append(newRunes, (ch-5-'a')%26+'a')
    }
    return string(newRunes)
}


// returns encoded string by shifting every character by 3 in the alphabet.
func EncodeShift3(s string) string {
    runes  := []rune(s)
    newRunes  := make([]rune, 0)
    for _, ch := range runes  {
        newRunes = append(newRunes, (ch+3-'a')%26+'a')
    }
    return string(newRunes)
}

// takes as input string encoded with EncodeShift3 function. Returns decoded string.
func DecodeShift3(s string) string {
    runes  := []rune(s)
    newRunes  := make([]rune, 0)
    for _, ch := range runes  {
        newRunes = append(newRunes, (ch-3-'a')%26+'a')
    }
    return string(newRunes)
}

func main() {
    fmt.Println(EncodeShift("hello")) // should print "mjqqt"
    fmt.Println(DecodeShift("mjqqt")) // should print "hello"
    fmt.Println(EncodeShift3("hello")) // should print "khoor"
    fmt.Println(DecodeShift3("khoor")) // should print "hello"
}
```

In this program, we have two functions `EncodeShift` and `DecodeShift` that encode and decode a string by shifting each character by 5 positions in the alphabet. We also have two functions `EncodeShift3` and `DecodeShift3` that encode and decode a string by shifting each character by 