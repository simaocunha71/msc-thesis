    var result []string
    for x != 0 {
        result = append(result, strconv.Itoa(x%base))
        x /= base
    }
    return string(reverse(result))
}

func reverse(s []string) []string {
    for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
        s[i], s[j] = s[j], s[i]
    }
    return s
}




The code defines a function ChangeBase that takes two parameters: x and base. It converts the decimal number x to the specified base. The function returns the string representation of the converted number. The base parameter is an integer less than 10.

To convert the number, the function uses a for loop to repeatedly divide x by the base and appends the remainder (x%base) to a result slice. The loop continues until x becomes 0. After the loop, the function reverses the order of the result slice and converts it to a string using the strconv.Itoa function. The reversed result is then returned.

The function also defines a separate function reverse, which takes a slice of strings and reverses its order. It uses a for loop to swap the first and last elements, then the second and second-to-last elements, and so on until the middle of the slice. Finally, it returns the reversed slice.

Here are some example test cases for the ChangeBase function:

ChangeBase(8, 3) returns '22'
ChangeBase(8, 2) returns '1000'
ChangeBase(7, 2) returns '111'


























































































































