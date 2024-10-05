
Your code looks good! Here are some minor suggestions:

In HasCloseElements, you can simplify the calculation of the distance by using math.Pow:
distance := math.Pow(numbers[i] - numbers[j], 2)

And then compare distance with threshold * threshold:
if distance < threshold*threshold {
    return true
}

In SeparateParenGroups, you don't need to convert the slice of runes to string when appending to the result. You can directly append the slice of runes:
result = append(result, current_string)

In TruncateNumber, you can use the math.Floor function to get the integer part of the number:
integerPart := math.Floor(number)

And then return the decimal part:
return number - integerPart

In Digitsum, you can use the unicode.IsUpper function to check if a character is an uppercase letter:
if unicode.IsUpper(c) {

And then convert the uppercase letter to its ASCII code using the int function:
sum += int(c)

Overall, your code looks good and is easy to understand. These suggestions are just minor improvements that can make your code more efficient and readable.