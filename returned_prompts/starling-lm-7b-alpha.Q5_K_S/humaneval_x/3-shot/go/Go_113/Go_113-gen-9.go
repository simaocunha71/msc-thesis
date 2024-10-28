    result := make([]string, 0)
    for _, s := range lst {
        result = append(result, fmt.Sprintf("the number of odd elements %dn the str%sng %d of the %dnput.",len(odd(s)),s,len(odd(s)),len(s)))
    }
    return result
}

func odd(s string) int {
    count := 0
    for _, r := range s {
        if r % 2 != 0 {
            count += 1
        }
    }
    return count
}



