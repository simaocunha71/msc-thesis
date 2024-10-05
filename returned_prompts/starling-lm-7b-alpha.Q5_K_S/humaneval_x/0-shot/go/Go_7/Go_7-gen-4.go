    var result []string

    for _, s := range stringList {
        if strings.Contains(s, substring) {
            result = append(result, s)
        }
    }

    return result
}



The FilterBySubstring function filters a list of strings only for ones that contain the given substring. It returns an array of strings that are filtered from the input list of strings. The function works by iterating over the input stringList. For each string in the stringList, it checks if the substring is present in the string using the Contains function from the strings package. If the substring is present, it adds the string to the result array using the append function. Finally, it returns the result array.

To test the function, you can use the following test cases:

FilterBySubstring([]string{}, "a") // should return []
FilterBySubstring([]string{"abc", "bacd", "cde", "array"}, "a") // should return ["abc", "bacd", "array"]

You can add these test cases to your code and print the result to see if the function is working correctly.

Here's an example of how to use the FilterBySubstring function:

inputList := []string{"abc", "bacd", "cde", "array"}
substring := "a"
result := FilterBySubstring(inputList, substring)
fmt.Println(result) // should print ["abc", "bacd", "array"]

In this example, we define an inputList of strings and a substring to search for. We then call the FilterBySubstring function with these inputs and store the result in the result variable. Finally, we print the result to the console.

Note that the FilterBySubstring function is case-sensitive, so it will only find substrings that match the exact case of the input string.

I hope this helps! Let me know if you have any more questions.

Here are some additional resources you might find helpful:
- Go strings package documentation: https://golang.org/pkg/strings/
- Go strings.Contains function documentation: https://golang.org/pkg/strings/#Contains
- Go append function documentation: https://golang.org/pkg/builtin/#