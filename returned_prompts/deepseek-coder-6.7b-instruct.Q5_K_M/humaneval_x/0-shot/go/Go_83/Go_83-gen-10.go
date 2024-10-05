    if n == 1 {
        return 1
    } else {
        return 2 * StartsOneEnds(n-1)
    }
}

func main() {
    fmt.Println(