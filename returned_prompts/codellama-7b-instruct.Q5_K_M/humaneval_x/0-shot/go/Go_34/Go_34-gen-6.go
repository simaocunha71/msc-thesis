
sort.Ints(l)
var result []int
for i := 0; i < len(l); i++ {
    if l[i] != l[i-1] {
        result = append(result, l[i])
    }
}
return result
}

