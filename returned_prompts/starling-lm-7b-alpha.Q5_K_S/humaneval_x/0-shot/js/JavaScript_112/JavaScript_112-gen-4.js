To solve this kata, you should follow these steps:

1. Create a new empty string, named result.
2. Iterate through the string s. For each character in s, if the character is not in the string c, add it to the result string.
3. Reverse the result string.
4. Compare the result string with the reversed result string. If they are equal, return (result, true). Otherwise, return (result, false).

Here is a step-by-step walkthrough for the provided examples:

Example 1:
For s = "abcde" and c = "ae", the result should be ('bcd', false).

1. Create a new empty string, named result. result = ""
2. Iterate through the string s. For each character in s, if the character is not in the string c, add it to the result string. In this case, the character 'a' is in the string c, and the character 'b' is not in the string c, so add 'b' to the result string. result = "b"
3. Reverse the result string. result = "b"
4. Compare the result string with the reversed result string. Since they are equal, return (result, true). However, in this case, the result is false.

Example 2:
For s = "abcdef" and c = "b", the result should be ('acdef', false).

1. Create a new empty string, named result. result = ""
2. Iterate through the string s. For each character in s, if the character is not in the string c, add it to the result string. In this case, the character 'a' is not in the string c, so add 'a' to the result string. result = "a"
3. Reverse the result string. result = "a"
4. Compare the result string with the reversed result string. Since they are equal, return (result, true). However, in this case, the result is false.

Example 3:
For s = "abcdedcba" and c = "ab", the result should be ('cdedc', true).

1. Create a new empty string, named result. result = ""
2. Iterate through the string s.