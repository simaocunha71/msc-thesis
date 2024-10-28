
Here's a simple solution for the first problem, it does not guarantee the smallest possible distance, but it's the most efficient I can think of.
func HasCloseElements(numbers []float64, threshold float64) bool {
    min, max := math.Inf(1), math.Inf(-1)
    for _, num := range numbers {
        min = math.Min(num, min)
        max = math.Max(num, max)
    }
    return max-min < threshold
}

The second problem is a bit more complex, and there are many possible solutions. Here's one that uses a map to keep track of the parentheses depths.
func SeparateParenGroups(paren_string string) []string {
    groups := make([]string, 0)
    stack := make([]rune, 0)
    for _, c := range paren_string {
        if c == '(' {
            stack = append(stack, c)
        } else if c == ')' {
            if len(stack) > 0 {
                stack = stack[:len(stack)-1]
                if len(stack) == 0 {
                    groups = append(groups, string(paren_string))
                    paren_string = paren_string[len(stack)+1:]
                }
            }
        }
    }
    return groups
}

The third problem can be solved with a simple loop and comparison.
func TruncateNumber(number float64) float64 {
    return number - math.Floor(number)
}

The fourth problem is also a bit complex, and there are many possible solutions. Here's one that uses a map to keep track of the numbers and their frequencies.
func FindClosestElements(numbers []float64) [2]float64 {
    freq := make(map[float64]int)
    for _, num := range numbers {
        freq[num]++
    }
    var min_dist float64 = math.Inf(1)
    var result [2]float64
   