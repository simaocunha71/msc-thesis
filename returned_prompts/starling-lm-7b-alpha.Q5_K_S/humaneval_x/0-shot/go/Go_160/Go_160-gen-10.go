    // 可以先根据 operator 和 operand 的长度来判断是否合法，
    // 如果长度不同，那么就直接返回 0，因为下面的计算是基于两者长度相同来进行的，
    if len(operator) != len(operand) - 1 {
        return 0
    }
    // 然后根据 operator 和 operand 中的元素来构造表达式，
    // 然后计算这个表达式的值，并返回。
    result := operand[0]
    for i := 0; i < len(operator); i++ {
        if operator[i] == "+" {
            result += operand[i+1]
        } else if operator[i] == "*" {
            result *= operand[i+1]
        } else if operator[i] == "-" {
            result -= operand[i+1]
        } else if operator[i] == "//" {
            result = result / operand[i+1]
        } else if operator[i] == "**" {
            result = math.Pow(float64(result), float64(operand[i+1]))
        }
    }
    return result
}

// 由于题目中没有给出 operator 和 operand 的长度是否相等，
// 而题目中的测试用例中，operator 和 operand 的长度是相等的。
// 因此，可以先根据 operator 和 operand 的长度来判断是否合法，
// 如果长度不同，那么就直接返回 0，因为下面的计算是基于两者长度相同来进行的，
// 然后根据 operator 和 operand 中的元素来构造表达式，
// 然后计算这个表达式的值，并返回。

// 所以，这道题目的关键在于如何构造表达式。
// 可以看出，这道题目是要求我们根据 operator