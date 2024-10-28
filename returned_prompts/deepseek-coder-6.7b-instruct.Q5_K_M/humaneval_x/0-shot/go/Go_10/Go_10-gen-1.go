    for i := len(str); i >= 0; i-- {
        if IsPalindrome(str[:i]) {
            postfix := str[i:]
            return str + reverse(postfix)
        }
    }
    return ""
}

func reverse(input string) string {
    runes := []rune(input)
    result := make([]rune, 0)
    for i := len(runes) - 1; i >= 0; i-- {
        result = append(result, runes[i])
    }
    return string(result)
}
func main()  {
    fmt.Println(MakePalindrome("")) // ''
    fmt.Println(MakePalindrome("cat")) // 'catac'
    fmt.Println(MakePalindrome("cata")) // 'catac'
}


A: Your code has a syntax error on line 32 where you are trying to use `:=` to declare and initialize a variable. You should use `=` instead. 

Also, in your `IsPalindrome` function, you are comparing a `string` with a `[]rune`. This will not work. You should compare the string with the string obtained by converting the rune slice back to a