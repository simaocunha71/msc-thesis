    count := 0

B:
    for _, c := range brackets {
        switch c {
        case '(':
            count++
        case ')':
            count--
        default:
            return false
        }

        if count < 0 {
            return false
        }
    }

    return count == 0
}

func main() {
    fmt.Println(CorrectBracketing("("))         // false
    fmt.Println(CorrectBracketing("()"))        // true
    fmt.Print