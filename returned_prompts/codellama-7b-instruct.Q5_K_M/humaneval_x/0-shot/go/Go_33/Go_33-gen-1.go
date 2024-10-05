for i := 0; i < len(l); i++ {
    if i % 3 == 0 {
        sort.Ints(l[i:(i+3)])
    }
}
return l
}
