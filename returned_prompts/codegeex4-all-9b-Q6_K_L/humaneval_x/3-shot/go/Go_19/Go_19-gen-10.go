    numberals := strings.Fields(numbers)
    var numbersToSort []int
    for _, numberal := range numberals {
        switch numberal {
        case "zero":
            numbersToSort = append(numbersToSort, 0)
        case "one":
            numbersToSort = append(numbersToSort, 1)
        case "two":
            numbersToSort = append(numbersToSort, 2)
        case "three":
            numbersToSort = append(numbersToSort, 3)
        case "four":
            numbersToSort = append(numbersToSort, 4)
        case "five":
            numbersToSort = append(numbersToSort, 5)
        case "six":
            numbersToSort = append(numbersToSort, 6)
        case "seven":
            numbersToSort = append(numbersToSort, 7)
        case "eight":
            numbersToSort = append(numbersToSort, 8)
        case "nine":
            numbersToSort = append(numbersToSort, 9)
        }
    }
    sort.Ints(numbersToSort)
    var sortedNumberals []string
    for _, number := range numbersToSort {
        switch number {
        case 0:
            sortedNumberals = append(sortedNumberals, "zero")
        case 1:
            sortedNumberals = append(sortedNumberals, "one")
        case 2:
            sortedNumberals = append(sortedNumberals, "two")
        case 3:
            sortedNumberals = append(sortedNumberals, "three")
        case 4:
            sortedNumberals = append(sortedNumberals, "four")
        case 5:
            sortedNumberals = append(sortedNumberals, "five")
        case 6:
            sortedNumberals = append(sortedNumberals, "six")
        case 7:
            sortedNumberals = append(sortedNumberals, "seven")
        case 8:
            sortedNumberals = append(sortedNumberals, "eight")
        case 9:
            sortedNumberals = append(sortedNumberals, "nine")
        }
    }
    return strings.Join(sortedNumberals, " ")
}

