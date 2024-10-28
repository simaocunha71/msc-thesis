
Here's an example of the function's behavior:

    console.log(findUniques("This is a test", "This is a trial"));
    // Output: " test"


Here's a function that meets the requirements:

    function findUniques(str1, str2) {
      const tokens1 = str1.split(" ");
      const tokens2 = str2.split(" ");
      const uniqueTokens = [];
      for (let i = 0; i < tokens1.length; i++) {
        let isUnique = true;
        for (let j = 0; j < tokens2.length; j++) {
          if (tokens1[i] === tokens2[j]) {
            isUnique = false;
            continue;
          }
        }
        if (isUnique) {
          uniqueTokens.push(tokens1[i]);
        }
      }
      return uniqueTokens.join(" ");
    }


Explanation:

    The function first splits the input strings into arrays of tokens using the space character as the separator.

    It then initializes an empty array called uniqueTokens to store the unique tokens from the first string.

    The function uses two nested for loops to compare each token from the first string with each token from the second string. If a match is found, the isUnique flag is set to false and the inner loop is exited using the continue statement.

    After the inner loop finishes, the function checks if the isUnique flag is still true. If it is, then the current token from the first string is unique and should be added to the uniqueTokens array.

    Finally, the function joins the uniqueTokens array into a string using a space as the separator and returns the result.

    This solution ensures that only the unique tokens from the first string that are not present in the second string are returned as a single space-separated string.












































































