    result := ""
    for _,char := range s{
        if !strings.ContainsRune(c,char){
            result += string(char)
        }
    }
    isPalindrome := result == reverse(result)
    return [2]interface{}{result,isPalindrome}
}

func reverse(input string) string {
    runes := []rune(input)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

