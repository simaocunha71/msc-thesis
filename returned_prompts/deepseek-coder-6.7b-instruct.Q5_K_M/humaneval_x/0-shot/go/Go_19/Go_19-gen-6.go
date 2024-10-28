    wordNumbers := map[string]int{
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

B:
    numberWords := map[int]string{
        0: "zero",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
    }

C:
    words := strings.Split(numbers, " ")
    var nums []int

D:
    for _, word := range words {
        nums = append(nums, wordNumbers[word])
    }

E:
    sort.Ints(nums)

F:
    var sortedStrings []string
    for _, num := range nums {
        sortedStrings = append(sortedStrings, numberWords[num])
    }

G:
    return strings.Join(sortedStrings, " ")
}

*/

func main() {
	fmt.Println(SortNumbers("three one five")) // 'one three five'
}

func SortNumbers(numbers string) string {
	wordNumbers := map[string]int{
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

	numberWords := map[int]string{
		0: "zero",
		1: "one",
		2: "two",
		3: "three",
		