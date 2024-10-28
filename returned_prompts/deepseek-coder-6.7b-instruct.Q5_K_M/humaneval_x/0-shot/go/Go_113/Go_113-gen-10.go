    var new_list []string
    for i, str := range lst {
        count := 0
        for _, char := range str {
            if (char - '0') % 2 != 0 {
                count++
            }
        }
        new_string := fmt.Sprintf("the number of odd elements %don the string %d of the input.", count, i+1)
        new_list = append(new_list, new_string)
    }
    return new_list
}


This code works by iterating over the list of strings. For each string, it counts the number of odd digits. Then it constructs a new string using the count. This new string is added to the list of results.

The count of odd digits is calculated by subtracting the ASCII value of '0' from the ASCII value of each digit. If the result is odd, then the digit is odd.

The new string is constructed using the Sprintf function from the fmt package. The format string includes placeholders for the count of odd digits and the number of the current string in the list.

Finally, the list of new strings is returned.

Note: This code assumes that the strings in the input list are composed of digits only. If this is not the case, the code may not work as expected.

The code is not optimized for large inputs as it does not use any advanced data structures or algorithms. It has a time complexity of O(n*m) where n is the number of strings in the input list and m is the length of the longest string.

Please note that the Sprintf function in Go does not support formatting placeholders like "4n" or "1n