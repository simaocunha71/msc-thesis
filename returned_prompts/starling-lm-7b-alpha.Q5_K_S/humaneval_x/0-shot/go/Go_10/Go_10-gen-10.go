    if IsPalindrome(str) {
        return str
    }
    var suffix []rune
    for i := len(str) - 1; i >= 0; i-- {
        suffix = append(suffix, str[i])
        if IsPalindrome(string(suffix)) {
            break
        }
    }
    return str + string(reverse(str[:len(str)-len(suffix):])) + string(suffix)
}

func reverse(str string) string {
    return strings.Join(strings.Split(str, ""), "")
}

MakePalindrome("")
// ""

MakePalindrome("cat")
// "catac"

MakePalindrome("cata")
// "catac"

MakePalindrome("cab")
// "caba"

MakePalindrome("cabaa")
// "cabaa"

MakePalindrome("cabaaa")
// "cabaac"

MakePalindrome("cabaaax")
// "cabaaaxca"

MakePalindrome("cabaaaxac")
// "cabaaaxacac"

MakePalindrome("axacabaaayaxaxca")
// "ayaxcaaxayacaaxayca"

MakePalindrome("acbayaaayayaxayca")
// "aycaayayayacayayayca"

MakePalindrome("ayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayayay