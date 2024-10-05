    number = math.Abs(number)  // convert to positive
    integerPart := math.Floor(number) // get integer part
    decimalPart := number - integerPart // subtract integer part from original to get decimal part

    return decimalPart
}

