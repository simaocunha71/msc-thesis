Here is the solution:
```javascript
const numericalLetterGrade = (grades) => {
  const letterGrades = [];
  grades.forEach(gpa => {
    if (gpa >= 4.0) {
      letterGrades.push('A+');
    } else if (gpa >= 3.7) {
      letterGrades.push('A');
    } else if (gpa >= 3.3) {
      letterGrades.push('A-');
    } else if (gpa >= 3.0) {
      letterGrades.push('B+');
    } else if (gpa >= 2.7) {
      letterGrades.push('B');
    } else if (gpa >= 2.3) {
      letterGrades.push('B-');
    } else if (gpa >= 2.0) {
      letterGrades.push('C+');
    } else if (gpa >= 1.7) {
      letterGrades.push('C');
    } else if (gpa >= 1.3) {
      letterGrades.push('C-');
    } else if (gpa >= 1.0) {
      letterGrades.push('D+');
    } else if (gpa >= 0.7) {
      letterGrades.push('D');
    } else if (gpa >= 0.0) {
      letterGrades.push('D-');
    } else {
      letterGrades.push('E');
    }
  });
  return letterGrades;
};
```
Explanation:
The function `numericalLetterGrade` takes an array of GPAs as input and returns an array of letter grades. It iterates over the input array and uses if-else statements to determine the corresponding letter grade for each GPA. The letter grades are then pushed to the `letterGrades` array and returned at the end.