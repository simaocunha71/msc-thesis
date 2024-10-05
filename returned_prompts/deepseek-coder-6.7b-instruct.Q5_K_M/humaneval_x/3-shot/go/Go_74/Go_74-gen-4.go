    totalChars := func(lst []string) int {
        total := 0
        for _, str := range lst {
            total += len(str)
        }
        return total
    }
    return func() []string {
        if totalChars(lst1) < totalChars(lst2) {
            return lst1
        }
        return lst2
    }()
}



