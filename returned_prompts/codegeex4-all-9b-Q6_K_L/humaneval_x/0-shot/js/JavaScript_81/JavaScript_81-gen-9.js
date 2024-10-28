```java
const numericalLetterGrade = (grades) => {
  let letterGrades = []
  for (let i = 0; i < grades.length; i++) {
    if (grades[i] == 4.0) {
      letterGrades.push('A+')
    } else if (grades[i] > 3.7) {
      letterGrades.push('A')
    } else if (grades[i] > 3.3) {
      letterGrades.push('A-')
    } else if (grades[i] > 3.0) {
      letterGrades.push('B+')
    } else if (grades[i] > 2.7) {
      letterGrades.push('B')
    } else if (grades[i] > 2.3) {
      letterGrades.push('B-')
    } else if (grades[i] > 2.0) {
      letterGrades.push('C+')
    } else if (grades[i] > 1.7) {
      letterGrades.push('C')
    } else if (grades[i] > 1.3) {
      letterGrades.push('C-')
    } else if (grades[i] > 1.0) {
      letterGrades.push('D+')
    } else if (grades[i] > 0.7) {
      letterGrades.push('D')
    } else if (grades[i] > 0.0) {
      letterGrades.push('D-')
    } else {
      letterGrades.push('E')
    }
  }
  return letterGrades
}
```
