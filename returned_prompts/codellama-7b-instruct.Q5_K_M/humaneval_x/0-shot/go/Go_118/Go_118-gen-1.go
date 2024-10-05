    for i := len(word) - 1; i >= 0; i-- {
        if isVowel(word[i]) {
            if !isVowel(word[i-1]) {
                return word[i : i+1]
            }
        }
    }
    return ""
}

func isVowel(s string) bool {
    for _, v := range s {
        if v == 'a' || v == 'e' || v == 'i' || v == 'o' || v == 'u' {
            return true
        }
    }
    return false
}

func main() {
    fmt.Println(GetClosestVowel("yogurt"))
    fmt.Println(GetClosestVowel("FULL"))
    fmt.Println(GetClosestVowel("quick"))
    fmt.Println(GetClosestVowel("ab"))
}


