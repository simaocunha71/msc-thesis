  let count = 0;
  let pos = 0;

  while ((pos = string.indexOf(substring, pos)) != -1) {
    count++;
    pos += substring.length;
  }

  return count;
}
```

These are some examples of JavaScript functions that can be used to solve specific problems. These functions can be used as a starting point for solving more complex problems or can be used as a reference to help with understanding how to solve a particular type of problem.

The first function, `hasCloseElements`, checks if there are any two numbers in a given list that are closer to each other than a given threshold. It does this by iterating through the list and checking if the absolute difference between any two numbers is less than the threshold. If it finds such a pair, it returns `true`. Otherwise, it returns `false`.

The second function, `separateParenGroups`, takes a string containing multiple groups of nested parentheses and separates them into separate strings. It does this by iterating through the string and keeping track of the current group and its depth. When it encounters a closing parenthesis, it checks if the current group is complete (i.e., the depth is 0). If it is, it adds the group to the result list and resets the current group. If the group is not complete, it continues to the next character.

The third function, `truncateNumber`, takes a positive floating-point number and returns its decimal part. It does this by using the modulo operator (`%`) to find the remainder of the number divided by 1.0.

The fourth function, `howManyTimes`, takes a string and a substring and returns the number of times the substring can be found in the string. It does this by iterating through the string and using the `indexOf` method to find the position of the substring. It then increments a count for each occurrence and continues to the next character until it has searched the entire string. If it finds the substring at the end of the string, it will return the correct count. If the substring is not found at all, it will return 0.