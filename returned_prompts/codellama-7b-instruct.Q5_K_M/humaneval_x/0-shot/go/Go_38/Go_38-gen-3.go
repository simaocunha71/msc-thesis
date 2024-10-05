    for {
        if len(s) == 0 {
            break
        }
        if len(s) == 1 {
            return s
        }
        if len(s) == 2 {
            return s[1:] + s[0]
        }
        if s[0] == s[2] && s[1] == s[0] {
            s = s[1:]
        } else {
            break A
        }
    }
    return s
}

// takes as input string encoded with EncodeCyclic function. Returns decoded string.
func DecodeCyclic(s string) string {

    for {
        if len(s) == 0 {
            break
        }
        if len(s) == 1 {
            return s
        }
        if len(s) == 2 {
            return s[1:] + s[0]
        }
        if s[0] == s[2] && s[1] == s[0] {
            s = s[1:]
        } else {
            break
        }
    }
    return s
}

func main() {
    s := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    fmt.Println(EncodeCyclic(s))
    fmt.Println(DecodeCyclic(EncodeCyclic(s)))
}
