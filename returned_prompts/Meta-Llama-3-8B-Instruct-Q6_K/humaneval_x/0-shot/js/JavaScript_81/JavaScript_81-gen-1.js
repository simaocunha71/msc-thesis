```
const numericalLetterGrade = (grades) => {
  const letterGrades = [];
  for (let i = 0; i < grades.length; i++) {
    let letterGrade = '';
    if (grades[i] >= 4) {
      letterGrade = 'A+';
    } else if (grades[i] >= 3.7) {
      letterGrade = 'A';
    } else if (grades[i] >= 3.3) {
      letterGrade = 'A-';
    } else if (grades[i] >= 3.0) {
      letterGrade = 'B+';
    } else if (grades[i] >= 2.7) {
      letterGrade = 'B';
    } else if (grades[i] >= 2.3) {
      letterGrade = 'B-';
    } else if (grades[i] >= 2.0) {
      letterGrade = 'C+';
    } else if (grades[i] >= 1.7) {
      letterGrade = 'C';
    } else if (grades[i] >= 1.3) {
      letterGrade = 'C-';
    } else if (grades[i] >= 1.0) {
      letterGrade = 'D+';
    } else if (grades[i] >= 0.7) {
      letterGrade = 'D';
    } else if (grades[i] >= 0.0) {
      letterGrade = 'D-';
    } else {
      letterGrade = 'E';
    }
    letterGrades.push(letterGrade);
  }
  return letterGrades;
}
```


The function goes through each GPA in the list, compares it to the GPA ranges, and assigns the corresponding letter grade. The letter grades are then pushed into a new array, which is returned at the end. This function works for any number of GPAs, not just the examples given.