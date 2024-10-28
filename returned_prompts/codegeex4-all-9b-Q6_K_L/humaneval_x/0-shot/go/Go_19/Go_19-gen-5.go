```go
func SortNumbers(numbers string) string{
    numStrs := strings.Fields(numbers)
    numVals := make([]int, len(numStrs))
    for i, numStr := range numStrs {
        switch numStr {
        case "zero":
            numVals[i] = 0
        case "one":
            numVals[i] = 1
        case "two":
            numVals[i] = 2
        case "three":
            numVals[i] = 3
        case "four":
            numVals[i] = 4
        case "five":
            numVals[i] = 5
        case "six":
            numVals[i] = 6
        case "seven":
            numVals[i] = 7
        case "eight":
            numVals[i] = 8
        case "nine":
            numVals[i] = 9
        default:
            panic("Invalid number string: " + numStr)
        }
    }
    sort.Ints(numVals)
    sortedNumStrs := make([]string, len(numVals))
    for i, numVal := range numVals {
        switch numVal {
        case 0:
            sortedNumStrs[i] = "zero"
        case 1:
            sortedNumStrs[i] = "one"
        case 2:
            sortedNumStrs[i] = "two"
        case 3:
            sortedNumStrs[i] = "three"
        case 4:
            sortedNumStrs[i] = "four"
        case 5:
            sortedNumStrs[i] = "five"
        case 6:
            sortedNumStrs[i] = "six"
        case 7:
            sortedNumStrs[i] = "seven"
        case 8:
            sortedNumStrs[i] = "eight"
        case 9:
            sortedNumStrs[i] = "nine"
        default:
            panic("Invalid number value: " + string(numVal))
        }
    }
    return strings.Join(sortedNumStrs, " ")
}
```