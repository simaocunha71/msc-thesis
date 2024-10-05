    return fmt.Sprintf("%b", binaryXor(a, b))
}

func binaryXor(a string, b string) (result int) {

B:
    for i := 0; i < len(a); i++ {
        if a[i] == b[i] {
            result |= 0
        } else {
            result |= 1 << uint(i)
        }
    }
    return
}


