    var evenList  []string 
    for _, word := range lst  {
        if len(word) % 2 == 0  {
            evenList = append(evenList, word)
        }
    }

    sort.Slice(evenList, func(i, j int) bool {
        return evenList[i] < evenList[j]
    })

    return evenList
}



