import (
    "strings"
)

// Given a positive integer, obtain its roman numeral equivalent as a string,
// and return it in lowercase.
// Restrictions: 1 <= num <= 1000
// 
// Examples:
// >>> IntToMiniRoman(19) == 'xix'
// >>> IntToMiniRoman(152) == 'clii'
// >>> IntToMiniRoman(426) == 'cdxxvi'
func IntToMiniRoman(number int) string {
    var i = 0
    var res []rune = make([]rune,0)
    
    if number < 1000 && number >= 1 {
        for i = 0; i <= number/9; i++ {
            res = append(res, "m"[i%9]+strings.Repeat("c", (8-i)%9)+"x")
        }
    } else if number == 1000 && number >= 1 {
         res = append(res, "d"+"m"+strings.Repeat("c", 3))
     } else {
        for i = 0; i <= number/900; i++ {
            res = append(res, strings.Repeat("m", (i%9)%10)+"cd"+
                               strings.Repeat("x", 2-(i%9)))
            
        }    
    }
        
    return string(res[0:]) + "lxxiv"
}