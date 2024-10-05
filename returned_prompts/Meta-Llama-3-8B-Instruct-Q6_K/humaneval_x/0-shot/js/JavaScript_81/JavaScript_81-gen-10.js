Here is a JavaScript function that can be used to solve this problem. This function iterates over the input array of GPAs and uses a series of if-else statements to determine the corresponding letter grade based on the GPA. The function returns an array of letter grades.

```javascript
const numericalLetterGrade = (grades) => {
  return grades.map(gpa => {
    if (gpa >= 4.0) {
      return 'A+';
    } else if (gpa > 3.7) {
      return 'A';
    } else if (gpa > 3.3) {
      return 'A-';
    } else if (gpa > 3.0) {
      return 'B+';
    } else if (gpa > 2.7) {
      return 'B';
    } else if (gpa > 2.3) {
      return 'B-';
    } else if (gpa > 2.0) {
      return 'C+';
    } else if (gpa > 1.7) {
      return 'C';
    } else if (gpa > 1.3) {
      return 'C-';
    } else if (gpa > 1.0) {
      return 'D+';
    } else if (gpa > 0.7) {
      return 'D';
    } else if (gpa > 0.0) {
      return 'D-';
    } else {
      return 'E';
    }
  });
};
```

You can test this function with the provided example:

```javascript
console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5])); // Output: ['A+', 'B', 'C-', 'C', 'A-']
```

This function works by iterating over the input array of GPAs and using a series of if-else statements to determine the corresponding letter grade based on the GPA. The function returns an array of letter grades. The if-else statements are ordered from highest GPA to lowest GPA, so that the function returns the correct letter grade for each GPA. The function also includes an else clause to handle the case where the GPA is 0.0 or less, in which case the letter grade is 'E'.