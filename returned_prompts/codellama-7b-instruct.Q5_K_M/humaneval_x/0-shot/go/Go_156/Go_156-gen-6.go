import "strconv"

func IntToMiniRoman(number int) string {
    if number < 1 || number > 1000 {
        return ""
    }

    var result string
    var num = number

    for num >= 1000 {
        result += "m"
        num -= 1000
    }

    for num >= 900 {
        result += "cm"
        num -= 900
    }

    for num >= 500 {
        result += "d"
        num -= 500
    }

    for num >= 400 {
        result += "cd"
        num -= 400
    }

    for num >= 100 {
        result += "c"
        num -= 100
    }

    for num >= 90 {
        result += "xc"
        num -= 90
    }

    for num >= 50 {
        result += "l"
        num -= 50
    }

    for num >= 40 {
        result += "xl"
        num -= 40
    }

    for num >= 10 {
        result += "x"
        num -= 10
    }

    for num >= 9 {
        result += "ix"
        num -= 9
    }

    for num >= 5 {
        result += "v"
        num -= 5
    }

    for num >= 4 {
        result += "iv"
        num -= 4
    }

    for num >= 1 {
        result += "i"
        num -= 1
    }

    return result
}

// Given a string, return its integer equivalent.
// Restrictions: str.length <= 6
// 
// Examples:
// >>> StrToInt("1234") == 1234
// >>> StrToInt("-1234") == -1234
// >>> StrToInt("0") == 0
func StrToInt(str string) int {

B