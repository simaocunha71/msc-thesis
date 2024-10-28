    for {
        if strings.Count(s, "") == 0 {
            break A
        }
        if strings.Count(s, "") != 0 {
            s = strings.Replace(s, "", "", 1)
        }
    }
    return s
}

func main() {
    fmt.Println(DecodeCyclic(EncodeCyclic("Hello")))
}
