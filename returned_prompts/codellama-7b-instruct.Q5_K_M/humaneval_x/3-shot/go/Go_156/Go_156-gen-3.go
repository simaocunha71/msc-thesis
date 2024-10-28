    var result string
    var ones string
    var tens string
    var hundreds string

    ones = "i v x"
    tens = "x l c"
    hundreds = "c d m"

    var ones_index int = (number % 10) - 1
    var tens_index int = ((number % 100 - ones_index) / 10) - 1
    var hundreds_index int = (number / 100) - 1

    result = strings.Replace(ones, " ", "", -1)
    result = strings.Replace(result, "i", ones[ones_index:ones_index+1], -1)

    result = strings.Replace(result, "x", tens[tens_index:tens_index+1], -1)
    result = strings.Replace(result, "l", tens[tens_index+1:tens_index+2], -1)
    result = strings.Replace(result, "c", tens[tens_index+2:tens_index+3], -1)

    result = strings.Replace(result, "c", hundreds[hundreds_index:hundreds_index+1], -1)
    result = strings.Replace(result, "d", hundreds[hundreds_index+1:hundreds_index+2], -1)
    result = strings.Replace(result, "m", hundreds[hundreds_index+2:hundreds_index+3], -1)

    return strings.ToLower(result)
}



