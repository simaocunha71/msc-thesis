```go
func CountUpper(s string) int {
    count := 0
    for i, c := range s {
        if strings.ToUpper(string(c)) == "A" && i%2 == 0 {
            count++
        }
    }
    return count
}
```


Explanation:
The function CountUpper takes a string s as input and returns the count of uppercase vowels in even indices.

Here's how the function works:

1. Initialize a variable count to 0, which will store the count of uppercase vowels in even indices.
2. Iterate over the input string s using a range-based for loop. The loop variable i takes the index of the character in the string, and c takes the character itself.
3. Inside the loop, use the strings.ToUpper function to convert the character c to uppercase. Then, check if the uppercase character is equal to "A" (which is the uppercase version of the vowel "a").
4. Additionally, check if the index i is even (i.e., i%2 == 0). If both conditions are true, increment the count variable.
5. After the loop finishes, return the count variable.

For example, if the input string is "aBCdEf", the function will iterate over the characters as follows:

* i = 0, c = 'a', count = 0 (not uppercase vowel and not even index)
* i = 1, c = 'B', count = 0 (uppercase vowel but not even index)
* i = 2, c = 'C', count = 0 (uppercase vowel but not even index)
* i = 3, c = 'd', count = 0 (not uppercase vowel and even index)
* i = 4, c = 'E', count = 0 (uppercase vowel but not even index)
* i = 5, c = 'f', count = 0 (not uppercase vowel and even index)

The function returns 0 because there are no uppercase vowels in even indices. If the input string were "aAaA", the function would return 2 because there are two uppercase vowels in even indices.