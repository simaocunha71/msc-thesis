    var i, j int
    for i = 0; i < len(operator); i++ {
        for j = i + 1; j < len(operator); j++ {
            if operator[i] == "+" {
                operand[i] += operand[j]
            } else if operator[i] == "*" {
                operand[i] *= operand[j]
            } else if operator[i] == "-" {
                operand[i] -= operand[j]
            } else if operator[i] == "//" {
                operand[i] /= operand[j]
            } else if operator[i] == "**" {
                operand[i] = int(math.Pow(float64(operand[i]), float64(operand[j])))
            }
        }
    }
    return operand[0]
}


























//Correct Solution:
import (
    "math"
)

func DoAlgebra(operator []string, operand []int) int {
    i, j := 0, 0
    for ; i < len(operator); i++ {
        if operator[i] == "+" {
            operand[i] += operand[j]
        } else if operator[i] == "*" {
            operand[i] *= operand[j]
        } else if operator[i] == "-" {
            operand[i] -= operand[j]
        } else if operator[i] == "//" {
            operand[i] /= operand[j]
        } else if operator[i] == "**" {
            operand[i] = int(math.Pow(float64(operand[i]), float64(operand[j])))
        }
        j++
    }
    return operand[0]
}


























































