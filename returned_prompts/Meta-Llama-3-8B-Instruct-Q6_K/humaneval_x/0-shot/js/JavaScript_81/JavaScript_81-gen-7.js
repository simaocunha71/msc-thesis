Here is a JavaScript function that can solve the problem:

```javascript
const numericalLetterGrade = (grades) => {
  const letterGrades = [];
  grades.forEach(grade => {
    if (grade >= 4.0) {
      letterGrades.push('A+');
    } else if (grade > 3.7) {
      letterGrades.push('A');
    } else if (grade > 3.3) {
      letterGrades.push('A-');
    } else if (grade > 3.0) {
      letterGrades.push('B+');
    } else if (grade > 2.7) {
      letterGrades.push('B');
    } else if (grade > 2.3) {
      letterGrades.push('B-');
    } else if (grade > 2.0) {
      letterGrades.push('C+');
    } else if (grade > 1.7) {
      letterGrades.push('C');
    } else if (grade > 1.3) {
      letterGrades.push('C-');
    } else if (grade > 1.0) {
      letterGrades.push('D+');
    } else if (grade > 0.7) {
      letterGrades.push('D');
    } else if (grade > 0.0) {
      letterGrades.push('D-');
    } else {
      letterGrades.push('E');
    }
  });
  return letterGrades;
};
```
This function takes a list of GPAs as input, and returns a list of letter grades. It iterates over each GPA, and uses a series of if-else statements to determine the corresponding letter grade based on the GPA. The letter grades are then pushed onto an array, which is returned at the end of the function.

You can call this function with a list of GPAs, like this:

```javascript
console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5])); // Output: ['A+', 'B', 'C-', 'C', 'A-']
```
This will output a list of letter grades corresponding to the input GPAs.