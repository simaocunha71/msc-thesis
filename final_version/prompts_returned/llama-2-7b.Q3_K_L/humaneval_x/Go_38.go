import (
    "math"
    "strings"
    "time"
)

// returns encoded string by cycling groups of three characters.
func EncodeCyclic(s string) string {
    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        groups = append(groups, s[3*i:int(math.Min(float64(3*i+3), float64(len(s))))])
    }
    newGroups := make([]string, 0)
    for _, group := range groups {
        runes := []rune(group)
        if len(group) == 3 {
            newGroups = append(newGroups, string(append(runes[1:], runes[0])))
        } else {
            newGroups = append(newGroups, group)
        }
    }
    return strings.Join(newGroups, "")
}

// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic(s string) string {
    groups := make([]string, 0)
    for i := 0; i < ((len(s) + 2) / 3); i++ {
        if len(groups) == 0 || (i-1)*3 >= groupLen && i*3 <= (groupLen+2)/3 {
            groups = append(groups, s[0:int(math.Min(float64((len(s)+2-1)), float64((3*i-1)-1)))]...)
        } else {
            groups = append(groups, s[0:int(math.Min(float64(3*(i+1)-1), float64((len(s)+2))) + 1)])
        }
    }
    return strings.Join(groups, "")
}