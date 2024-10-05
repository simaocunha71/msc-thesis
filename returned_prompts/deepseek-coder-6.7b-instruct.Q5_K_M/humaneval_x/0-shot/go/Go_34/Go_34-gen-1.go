     sort.Ints(l)
     j := 0

B:
     for i := 1; i < len(l); i++ {
         if l[j] == l[i] {
            continue
        