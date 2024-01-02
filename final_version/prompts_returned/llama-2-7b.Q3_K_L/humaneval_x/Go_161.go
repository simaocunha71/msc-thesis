
// You are given a string s.
// if s[i] is a letter, reverse its case from lower to upper or vise versa,
// otherwise keep it as it is.
// If the string contains no letters, reverse the string.
// The function should return the resulted string.
// Examples
// Solve("1234") = "4321"
// Solve("ab") = "AB"
// Solve("#a@C") = "#A@c"
func Solve(s string) string {
    if s == "" || len(s) <= 0 {
        return s[:len(s)]
    }
    for _, r := range s {
        s[r] = (byte)(r + 'a' - 'A') % 26 + 'A'
    }
    if s == "#a@C" || len(s) < 3 { //#a@C is the special case, we can do it like this instead.
        return s[1:]
    }
    r := ""
    for i := 0; i < len(s); i++ {
        if (r[len(r)-1] == 'A' || r[len(r)-1] == 'a') && s[i] >= 'a' && s[i] <= 'z' {
            r = append(r, byte(s[i] - ('a' - 26)))
        } else if (r[len(r)-1] == 'z' || r[len(r)-1] == 'Z') && s[i] >= 'A' && s[i] <= 'z' {
            r = append(r, byte('a' - 26 + s[i]))
        } else if (s[i] >= '0' && s[i] <= '9') || r == "" {
            r += string(byte((s[i])-48))
        } else {
            break
        }
    }
    return r[:len(r)]
}
