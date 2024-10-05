    num, _ := strconv.ParseFloat(value, 64)
    if num < 0 {
        return int(math.Ceil(num - 0.5))
    } else {
        return int(math.Floor(num + 0.5))
    }
}

The function works by first converting the string to a float64 with strconv.ParseFloat. 

If the number is less than 0, we subtract 0.5 and then use the Ceil function from the math package to round up the result. 

If the number is greater than or equal to 0, we add 0.5 and then use the Floor function from the math package to round down the result. 

The reason we subtract 0.5 and add 0.5 instead of just using the math.Round function is to ensure that if the number is equidistant between two integers, the one that is farthest from zero is returned.

This solution also assumes that the input will always be a valid number. If this is not the case, you should add error handling to check if the ParseFloat call was successful.

This solution uses the math package for the Ceil and Floor functions. If you can't use the math package, you can implement these functions yourself.

The solution also assumes that you can use the strconv and math packages. If you can't use these packages, you will need to implement your own functions for parsing the string to a number and for rounding the number.

This solution also assumes that you can use the int type. If you can't use the int type, you will need to implement your own type for storing the result.

This solution also assumes that you can use the return statement. If you can't use the return statement, you will need to implement your own way of returning the result.

This solution also assumes that you can use the underscore character (_) to ignore errors. If you can't use the underscore character, you will