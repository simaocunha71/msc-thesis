    xNum, xDen := SplitFraction(x)
    nNum, nDen := SplitFraction(n)

    return (xNum * nDen) == (nNum * xDen)
}

func SplitFraction(fraction string) (int, int) {
    parts := strings.Split(fraction, "/")
    num, _ := strconv.Atoi(parts[0])
    den, _ := strconv.Atoi(parts[1])
    return num, den
}

I'm trying to implement this in Go. I am new to Go programming. Could anyone help me with this code? I have the following questions:
1) In the HasCloseElements function, why are we starting the inner loop from i+1 instead of 0?
2) What is the use of the keyword "range" in the SeparateParenGroups function?
3) In the TruncateNumber function, why are we using math.Mod function?
4) In the Simplify function, what is the purpose of the SplitFraction function?

A: 1) The inner loop starts from i+1 instead of 0 because we want to compare every element in the list with every other element that comes after it. If we started from 0, we would be comparing an element with itself, which doesn't make sense.

2) The "range" keyword in Go is used for looping over items in collections such as arrays or slices. The syntax is "for index, value := range collection", where "index" is the index of the current item in the collection and "value" is the value of the current item.

3) The math.Mod function is used to find the remainder of division. In this case, we use it to find the decimal part of the number, because the remainder of division by 1 is the decimal part.

4) The SplitFraction function is used to split the string representation of a fraction into the numerator and denominator. This is done because we need to perform mathematical operations on these values. The "strings.Split" function is used to split the string at the "/" character, and "strconv.Atoi" is used to convert the numerator and denominator from strings to integers.

