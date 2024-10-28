    // Convert the numbers in the string to integers
    nums := strings.Split(numbers, " ")
    // Create a slice of integers from the string
    ints := make([]int, len(nums))
    for i, v := range nums {
        switch v {
        case "zero":
            ints[i] = 0
        case "one":
            ints[i] = 1
        case "two":
            ints[i] = 2
        case "three":
            ints[i] = 3
        case "four":
            ints[i] = 4
        case "five":
            ints[i] = 5
        case "six":
            ints[i] = 6
        case "seven":
            ints[i] = 7
        case "eight":
            ints[i] = 8
        case "nine":
            ints[i] = 9
        }
    }
    // Sort the slice
    sort.Ints(ints)
    // Convert the sorted slice back to a string
    ret := strings.Builder{}
    for _, v := range ints {
        switch v {
        case 0:
            ret.WriteString("zero ")
        case 1:
            ret.WriteString("one ")
        case 2:
            ret.WriteString("two ")
        case 3:
            ret.WriteString("three ")
        case 4:
            ret.WriteString("four ")
        case 5:
            ret.WriteString("five ")
        case 6:
            ret.WriteString("six ")
        case 7:
            ret.WriteString("seven ")
        case 8:
            ret.WriteString("eight ")
        case 9:
            ret.WriteString("nine ")
        }
    }
    return ret.String()
}

func main() {
    fmt.Println(SortNumbers("three one five"))
}






































