  if (a + b > c && a + c > b && b + c > a) {
    const s = (a + b + c) / 2;
    return (Math.sqrt(s * (s - a) * (s - b) * (s - c))).toFixed(2);
  } else {
    return -1;
  }
}
```
These are the solutions to the given problems in JavaScript. The explanations are provided in the comments.

1. **hasCloseElements**: This function checks if there are any two numbers in a given list that are closer to each other than a given threshold. It iterates through each pair of numbers in the list and checks if their difference is less than the threshold. If it finds such a pair, it returns `true`. If it doesn't find any such pair, it returns `false`.

2. **separateParenGroups**: This function takes a string containing multiple groups of nested parentheses and separates them into separate strings. It iterates through each character in the string, and when it encounters an open parenthesis, it increments a depth counter. When it encounters a close parenthesis, it decrements the depth counter. When the depth counter becomes zero, it means that a group of parentheses has been closed, and it adds the current group to the result list.

3. **truncateNumber**: This function takes a floating-point number and returns its decimal part. It uses the modulo operator (`%`) to get the remainder of the division of the number by 1.0. This remainder is the decimal part of the number.

4. **triangleArea**: This function takes the lengths of the three sides of a triangle and returns its area. It first checks if the three sides form a valid triangle by checking if the sum of any two sides is greater than the third side. If they do, it calculates the area using Heron's formula and returns it rounded to 2 decimal points. If they don't, it returns -1.