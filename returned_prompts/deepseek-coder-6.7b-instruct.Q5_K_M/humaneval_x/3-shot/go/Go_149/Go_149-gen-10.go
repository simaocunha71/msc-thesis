    var evenStrings []string

    for _, str := range lst {
        if len(str)%2 == 0 {
            evenStrings = append(evenStrings, str)
        }
    }

    sort.Slice(evenStrings, func(i, j int) bool {
        if len(evenStrings[i]) == len(evenStrings[j]) {
            return evenStrings[i] < evenStrings[j]
        }
        return len(evenStrings[i]) < len(evenStrings[j])
    })

    return evenStrings
}



