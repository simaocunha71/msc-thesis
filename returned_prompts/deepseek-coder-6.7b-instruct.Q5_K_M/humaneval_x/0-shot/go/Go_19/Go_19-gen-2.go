    words := strings.Fields(numbers)
    sort.Slice(words, func(i, j int) bool {
        return numMap[words[i]] < numMap[words[j]]
    })
    return strings.Join(words, " ")
}

var numMap = map[string]int{
    "zero":  0,
    "one":   1,
    "two":   2,
    "three": 3,
    "four":  4,
    "five":  5,
    "six":   6,
    "seven": 7,
    "eight": 8,
    "nine":  9,
}

func main() {
    fmt.Println(SortNumbers("three one five"))
}



