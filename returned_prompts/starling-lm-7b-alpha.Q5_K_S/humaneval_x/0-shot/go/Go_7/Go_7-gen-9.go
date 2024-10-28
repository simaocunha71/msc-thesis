    var result []string
    for _, str := range stringList {
        if strings.Contains(str, substring) {
            result = append(result, str)
        }
    }
    return result
}




Here is a Go program that filters an input list of strings only for ones that contain a given substring.

The `FilterBySubstring` function takes two arguments: `stringList`, which is the input list of strings, and `substring`, which is the substring we want to search for within each string.

Inside the function, we initialize an empty slice called `result` to store the filtered strings. We then loop through each string in `stringList` using a `for` loop and the `range` keyword. For each string, we use the `strings.Contains` function to check if the `substring` is present in the string. If it is, we append the string to the `result` slice using the `append` function.

Finally, we return the `result` slice, which contains all the strings from the input list that contain the given substring.

To test the `FilterBySubstring` function, we use a series of print statements to display the result of calling the function with different inputs. In the first print statement, we call the function with an empty `stringList` and the substring `'a'`, which should return an empty list. In the second print statement, we call the function with a list of strings `['abc', 'bacd', 'cde', 'array']` and the substring `'a'`, which should return `['abc', 'bacd', 'array']`.

Overall, this program demonstrates a simple and effective way to filter a list of strings based on the presence of a specific substring.




















































































































