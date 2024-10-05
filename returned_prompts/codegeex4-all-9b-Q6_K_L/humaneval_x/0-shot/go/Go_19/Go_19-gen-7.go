```go
func SortNumbers(numbers string) string{
    numStrings := strings.Fields(numbers)
    numVals := make([]int, 0, len(numStrings))
    for _, numStr := range numStrings {
        switch numStr {
        case "zero":
            numVals = append(numVals, 0)
        case "one":
            numVals = append(numVals, 1)
        case "two":
            numVals = append(numVals, 2)
        case "three":
            numVals = append(numVals, 3)
        case "four":
            numVals = append(numVals, 4)
        case "five":
            numVals = append(numVals, 5)
        case "six":
            numVals = append(numVals, 6)
        case "seven":
            numVals = append(numVals, 7)
        case "eight":
            numVals = append(numVals, 8)
        case "nine":
            numVals = append(numVals, 9)
        }
    }
    sort.Ints(numVals)
    numStrings = numStrings[:0]
    for _, val := range numVals {
        switch val {
        case 0:
            numStrings = append(numStrings, "zero")
        case 1:
            numStrings = append(numStrings, "one")
        case 2:
            numStrings = append(numStrings, "two")
        case 3:
            numStrings = append(numStrings, "three")
        case 4:
            numStrings = append(numStrings, "four")
        case 5:
            numStrings = append(numStrings, "five")
        case 6:
            numStrings = append(numStrings, "six")
        case 7:
            numStrings = append(numStrings, "seven")
        case 8:
            numStrings = append(numStrings, "eight")
        case 9:
            numStrings = append(numStrings, "nine")
        }
    }
    return strings.Join(numStrings, " ")
}
```