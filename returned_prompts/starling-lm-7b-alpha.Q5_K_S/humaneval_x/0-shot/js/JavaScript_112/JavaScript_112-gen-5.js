To solve this problem we need to follow the steps below:

1. Create a result string by removing all the characters in s that are equal to any character in c.
2. Create a reversed result string by reversing the result string.
3. Check if the result string is equal to the reversed result string.
4. Return a tuple containing the result string and true/false for the check.

Here's the detailed step-by-step solution:

1. Initialize an empty string named "result".
2. Iterate through each character in s.
3. If the current character in s is not equal to any character in c, append the current character to the "result" string.
4. Reverse the "result" string using the .split(), .reverse(), and .join() methods. Let's call the reversed result string "reversedResult".
5. Check if the "result" string is equal to the "reversedResult" string. If they are equal, return a tuple containing the "result" string and true. Otherwise, return a tuple containing the "result" string and false.

Here's the JavaScript code that implements the above solution:

function reverseDelete(s, c) {
  let result = "";
  for (let i = 0; i < s.length; i++) {
    if (c.indexOf(s[i]) === -1) {
      result += s[i];
    }
  }
  const reversedResult = result.split("").reverse().join("");
  return [result, result === reversedResult];
}

The above code defines a function named "reverseDelete" that takes two parameters: "s" and "c". It initializes an empty string named "result" and iterates through each character in "s". If the current character in "s" is not found in "c", it appends the character to the "result" string. After iterating through all the characters in "s", it reverses the "result" string using the .split(), .reverse(), and .join() methods and stores the result in the "reversedResult" variable. Finally, it returns a tuple containing the "result" string and true/false for the check, which is determined by comparing the "result" string with the "reversedResult"