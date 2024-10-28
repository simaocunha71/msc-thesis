  let letterGrades = [];
  grades.forEach(grade => {
    if (grade >= 4.0) {
      letterGrades.push('A+');
    } else if (grade >= 3.7) {
      letterGrades.push('A');
    } else if (grade >= 3.3) {
      letterGrades.push('A-');
    } else if (grade >= 3.0) {
      letterGrades.push('B+');
    } else if (grade >= 2.7) {
      letterGrades.push('B');
    } else if (grade >= 2.3) {
      letterGrades.push('B-');
    } else if (grade >= 2.0) {
      letterGrades.push('C+');
    } else if (grade >= 1.7) {
      letterGrades.push('C');
    } else if (grade >= 1.3) {
      letterGrades.push('C-');
    } else if (grade >= 1.0) {
      letterGrades.push('D+');
    } else if (grade >= 0.7) {
      letterGrades.push('D');
    } else if (grade >= 0.0) {
      letterGrades.push('D-');
    } else {
      letterGrades.push('E');
    }
  });
  return letterGrades;
}
} // End of the code
```
This code contains four separate problems and their solutions. Here's a brief description of each problem:

1. **hasCloseElements**: This function checks if there are any two numbers in a given list that are closer to each other than a given threshold.

2. **separateParenGroups**: This function separates a string containing multiple groups of nested parentheses into separate strings.

3. **truncateNumber**: This function returns the decimal part of a given positive floating-point number.

4. **numericalLetterGrade**: This function converts a list of GPAs into a list of letter grades according to a given table.