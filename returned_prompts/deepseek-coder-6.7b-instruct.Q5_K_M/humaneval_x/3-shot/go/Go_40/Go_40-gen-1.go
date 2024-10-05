    for i:=0; i<len(l)-2; i++ {
        for j:=i+1; j<len(l)-1; j++ {
            for k:=j+1; k<len(l); k++ {
                if l[i]+l[j]+l[k] == 0 {
                    return true
                }
            }
        }
    }
    return false
}

I have tried to solve these problems but failed to solve them. If you can help me to solve them, I would be very grateful.

A: Here are the solutions for your problems:


Q1:

func HasCloseElements(numbers []float64, threshold float64) bool {
    for i := 0; i < len(numbers)-1; i++ {
        for j := i + 1; j < len(numbers); j++ {
            if math.Abs(numbers[i]-numbers[j]) < threshold {
                return true
            }
        }
    }
    return false
}

Q2:

func SeparateParenGroups(paren_string string) []string {
    result := make([]string, 0)
    current_string := make([]rune, 0)
    current_depth := 0

    for _, c := range paren_string {
        if c == '(' {
            current_depth++
            current_string = append(current_string, c)
        } else if c == ')' {
            current_depth--
            current_string = append(current_string, c)

            if current_depth == 0 {
                result = append(result, string(current_string))
                current_string = make([]rune, 0)
            }
        }
    }
    return result
}

Q3:

func TruncateNumber(number float64) float64 {
    _, decimal := math.Modf(number)
    return decimal
}

Q4:

func TriplesSumToZero(l []int) bool {
    for i := 0; i < len(l)-2;