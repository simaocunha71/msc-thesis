
Your solutions look good, but I'd suggest some improvements:

Avoid using raw loops when possible. Go's standard library has a lot of handy functions that can make your code more readable.

For example, in HasCloseElements you can use sort.Slice to sort the slice of numbers and then check if any two adjacent numbers are closer than the threshold.
func HasCloseElements(numbers []float64, threshold float64) bool {
    if len(numbers) < 2 {
        return false
    }

    sort.Float64s(numbers)

    for i := 1; i < len(numbers); i++ {
        if numbers[i]-numbers[i-1] < threshold {
            return true
        }
    }

    return false
}

In SeparateParenGroups you can use strings.Builder to build the strings, which is more efficient than appending to a slice of runes.

func SeparateParenGroups(parenString string) []string {
    var result []string
    var builder strings.Builder
    currentDepth := 0

    for _, c := range parenString {
        if c == '(' {
            currentDepth++
        } else if c == ')' {
            currentDepth--
        }

        builder.WriteRune(c)

        if currentDepth == 0 {
            result = append(result, builder.String())
            builder.Reset()
        }
    }

    return result
}

In TruncateNumber, you can use strconv.FormatFloat to format the number as a string and then parse it back to a float64. This is more accurate than using math.Mod.

func TruncateNumber(number float64) float64 {
    s := strconv.FormatFloat(number, 'f', -1, 64)
    i, _ := strconv.ParseFloat(s, 64)
    return number - i
}

In Longest you can use a map to track the longest string, which is more efficient than iterating over the slice twice.

func Longest(strings []string) *string {
    if len(strings) == 0 {
        return nil
    }

    longest := strings[0]
    for _, s := range strings {
        if len(s) > len(longest) {
            longest = s