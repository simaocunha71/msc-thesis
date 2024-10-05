import (
    "strings"
)

func ReverseDelete(s, c string) (string, bool) {
    s = strings.Map(func(r rune) rune {
        for _, cr := range c {
            if r == cr {
                return -1
            }
        }
        return r
    }, s)
    return s, strings.HasPrefix(s, strings.Reverse(s))
}

































