    sort.Ints(l)

B:
    var i int
    var j int
    for i = 1; i < len(l); i++ {
        if l[i] != l[i-1] {
            l[j] = l[i-1]
            j++
        }
    }
    l[j] = l[len(l)-1]
    return l[:j+1]
}

