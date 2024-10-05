    for i := range a {
        if a[i] != b[i] {
            return "Error"
        }
    }

    return a
}

func main() {
    fmt.Println(StringXor("010",