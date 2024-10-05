
The code is quite good, but it could be made more efficient by avoiding the conversions back and forth from strings and numbers. Here’s a version that does that:

func SortNumbers(numbers string) string {
    words := strings.Fields(numbers)
    nums := make([]int, len(words))
    for i, word := range words {
        switch word {
        case "zero":
            nums[i] = 0
        case "one":
            nums[i] = 1
        case "two":
            nums[i] = 2
        case "