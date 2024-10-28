    res := []rune(s)
    for _, r := range c {
        for i, rr := range res {
            if rr == r {
                res = append(res[:i], res[i+1:]...)
                break
            }
        }
    }
    return [2]interface{}{string(res), isPalindrome(res)}
}

func isPalindrome(res []rune) bool {
    n := len(res)
    for i := 0; i < n/2; i++ {
        if res[i] != res[n-i-1] {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(ReverseDelete("abccba", "ac"))
}

func ReverseDelete(s, c string) [2]interface{} {
    res := []rune(s)
    for _, r := range c {
        for i := 0; i < len(res); i++ {
            if res[i] == r {
                res = append(res[:i], res[i+1:]...)
                break
            }
        }
    }
    return [2]interface{}{string(res), isPalindrome(res)}
}

func isPalindrome(res []rune) bool {
    n := len(res)
    for i := 0; i < n/2; i++ {
        if res[i] != res[n-i-1] {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(ReverseDelete("abccba", "ac"))
}








































































































