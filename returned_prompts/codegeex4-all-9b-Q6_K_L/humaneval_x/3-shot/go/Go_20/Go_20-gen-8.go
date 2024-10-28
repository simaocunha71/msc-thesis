
import "math"

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := range numbers {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}

func SeparateParenGroups(paren_string string) []string {
    var res []string
    var stack []rune
    for _, c := range paren_string {
        if c == '(' {
            stack = append(stack, c)
        } else if c == ')' {
            var buf []rune
            buf = append(buf, '(')
            buf = append(buf, stack...)
            buf = append(buf, ')')
            res = append(res, string(buf))
            stack = stack[:0]
        }
    }
    return res
}

func TruncateNumber(number float64) float64 {
    return math.Mod(number, 1)
}

func FindClosestElements(numbers []float64) [2]float64 {
    if len(numbers) < 2 {
        return [2]float64{}
    }
    var minDiff float64 = math.Inf(1)
    var result [2]float64
    for i := range numbers {
        for j := i + 1; j < len(numbers); j++ {
            if diff := math.Abs(numbers[i]-numbers[j]); diff < minDiff {
                minDiff = diff
                result[0] = numbers[i]
                result[1] = numbers[j]
            }
        }
    }
    return result
}