for {
    for i := 0; i < len(s); i++ {
        if s[i] == s[i-1] && s[i] == s[i-2] {
            s = strings.Replace(s, s[i-1:i+1], "", 1)
            continue A
        }
    }
    break
}
return s
}

// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic2(s string) string {
    for {
        if len(s) > 2 {
            if s[0] == s[1] && s[0] == s[2] {
                s = s[3:]
                continue
            }
        }
        break
    }
    return s
}

// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic3(s string) string {
    for {
        if len(s) > 2 {
            if s[0] == s[1] && s[0] == s[2] {
                s = s[3:]
            } else {
                break
            }
        }
    }
    return s
}

// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic4(s string) string {
    for {
        if len(s) > 2 {
            if s[0] == s[1] && s[0] == s[2] {
                s = s[3:]
            } else {
                break
            }
        }
    }
    return s
}

// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic5(s string) string {
    for {
        if len(s) > 2 {
            if s[0] == s[1] && s[0] == s[2] {
                s = s[3:]
            } else {
                break
            }
        }
    }
    return s
}

// takes as input string encoded