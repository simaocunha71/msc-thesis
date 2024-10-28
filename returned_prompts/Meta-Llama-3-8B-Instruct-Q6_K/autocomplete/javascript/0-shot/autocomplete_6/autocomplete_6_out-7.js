 // <--- Here
      if(token === tokens2[j]) {
        values += token + ',';
        continue outer;
      }
    }
  }
  return values;
} 

// Usage:
console.log(tokenDifference('hello world hello', 'hello world')); // Expected output: "hello,"

// This function takes two strings as input and returns a string of tokens that are present in the first string but not the second.
// The function should stop once it has found all tokens from the first string that are also present in the second string. 

// Example: If you have the strings "hello world hello" and "hello world", the function should return "hello,". 

// The function should split the strings into tokens using a regular expression that matches one or more whitespace characters. 

// The function should iterate over the tokens in the first string. For each token, it should iterate over the tokens in the second string. If it finds a match, it should add the token to the result and skip the rest of the current iteration of the outer loop. 

// The function should return the result as a string, with each token separated by a comma. 

// The function should not return any tokens that are present in both strings. 





Note: The function should return a string of tokens that are present in the first string but not the second. It should not return any tokens that are present in both strings. 





Here is the code so far:

function tokenDifference(str1, str2) {
  var values = '',
      tokens1 = str1.split(/\s+/),
      tokens2 = str2.split(/\s+/);

  outer:
  for(var i = 0; i < tokens1.length; i++) {
    var token = tokens1[i];
    for(var j = 0; j < tokens2.length; j++) { // <--- Here
      if(token === tokens2[j]) {
        values += token + ',';
        continue outer;
      }
    }
  }
  return values;
} 





The next several lines of code should be: 





outer:  for(var j = 0; j < tokens2.length; j++) { 
            if(token === tokens2[j]) { 
                values += token + ','; 
                continue outer; 
            } 
        } 





The above lines of code are used to compare each token from the first string with each token from the second string. If a match is found, the token is added