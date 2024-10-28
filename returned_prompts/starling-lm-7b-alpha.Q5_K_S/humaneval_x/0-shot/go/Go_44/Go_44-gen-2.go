    var (
        res string
        tmp int
    )
    for x > 0 {
        tmp = x % base
        res = strconv.Itoa(tmp) + res
        x /= base
    }
    return res
}





In the above code, the function ChangeBase is used to convert a number in base 10 to another base. The function uses a for loop to repeatedly calculate the remainder of the input number divided by the base, and append the result to the beginning of the result string. Finally, the function returns the resulting string.


The code can be used as follows:
To convert a number in base 8 to base 3, you can call ChangeBase(8, 3). The function will return the string '22', which represents the binary representation of the number 8.
To convert a number in base 8 to base 2, you can call ChangeBase(8, 2). The function will return the string '1000', which represents the binary representation of the number 8.
To convert a number in base 7 to base 2, you can call ChangeBase(7, 2). The function will return the string '111', which represents the binary representation of the number 7.





The code uses the strconv.Itoa() function to convert the remainder of the division to a string. This function takes an integer as input and returns a string representation of the integer.

The code uses a for loop to repeatedly calculate the remainder of the division and append the result to the beginning of the result string. This is done until the input number becomes 0, at which point the function returns the resulting string.


The complexity of the ChangeBase function is O(log(x)), where x is the input number. This is because the for loop runs until the input number becomes 0, and the number of iterations is determined by the number of digits in the binary representation of the input number.







In the above code, the function ChangeBase is used to convert a number in base 10 to another base. The function uses a for loop to repeatedly calculate the remainder of the input number divided by the base, and append the result to the beginning of the result string. Finally, the function returns the resulting string.
