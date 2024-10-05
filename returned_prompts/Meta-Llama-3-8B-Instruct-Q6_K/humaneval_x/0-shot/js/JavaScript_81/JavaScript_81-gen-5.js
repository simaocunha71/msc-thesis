Here is a JavaScript function that will solve the problem:

```javascript
const numericalLetterGrade = (grades) => {
  const letterGrades = [];
  grades.forEach((gpa) => {
    if (gpa >= 4.0) {
      letterGrades.push('A+');
    } else if (gpa > 3.7) {
      letterGrades.push('A');
    } else if (gpa > 3.3) {
      letterGrades.push('A-');
    } else if (gpa > 3.0) {
      letterGrades.push('B+');
    } else if (gpa > 2.7) {
      letterGrades.push('B');
    } else if (gpa > 2.3) {
      letterGrades.push('B-');
    } else if (gpa > 2.0) {
      letterGrades.push('C+');
    } else if (gpa > 1.7) {
      letterGrades.push('C');
    } else if (gpa > 1.3) {
      letterGrades.push('C-');
    } else if (gpa > 1.0) {
      letterGrades.push('D+');
    } else if (gpa > 0.7) {
      letterGrades.push('D');
    } else if (gpa > 0.0) {
      letterGrades.push('D-');
    } else {
      letterGrades.push('E');
    }
  });
  return letterGrades;
};

console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5])); // Output: ['A+', 'B', 'C-', 'C', 'A-']
```

This function uses a simple if-else chain to check the GPA and assign the corresponding letter grade. The grades are pushed into an array and returned at the end. The function also logs the output to the console. You can call this function with a list of GPAs to get the corresponding letter grades.