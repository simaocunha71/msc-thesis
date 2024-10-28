    var evens  []int 
    for i := range l  {
        if i % 2 == 0  {
            evens  = append(evens, l[i])
        }
    }
    sort.Ints(evens)

    j := 0
    for i := range l  {
        if i % 2 == 0  {
            l[i] = evens[j]
            j++
        }
    }

    return l
}



