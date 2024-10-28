for i := 0; i < len(x); i++ {
    for j := 0; j < len(x); j++ {
        if x[i] == x[j] && i != j {
            x = append(x[:i], x[i+1:]...)
            i--
            goto A
        }
    }
}
sort.Ints(x)
return x
}
