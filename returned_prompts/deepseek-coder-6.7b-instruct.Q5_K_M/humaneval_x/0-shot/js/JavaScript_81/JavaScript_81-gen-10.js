  let finalGrades = []
  grades.forEach((grade) => {
    if (grade === 4.0) {
      finalGrades.push('A+')
    } else if (grade > 3.7) {
      finalGrades.push('A')
    } else if (grade > 3.3) {
      finalGrades.push('A-')
    } else if (grade > 3.0) {
      finalGrades.push('B+')
    } else if (grade > 2.7) {
      finalGrades.push('B')
    } else if (grade > 2.3) {
      finalGrades.push('B-')
    } else if (grade > 2.0) {
      finalGrades.push('C+')
    } else if (grade > 1.7) {
      finalGrades.push('C')
    } else if (grade > 1.3) {
      finalGrades.push('C-')
    } else if (grade > 1.0) {
      finalGrades.push('D+')
    } else if (grade > 0.7) {
      finalGrades.push('D')
    } else if (grade > 0.0) {
      finalGrades.push('D-')
    } else {
      finalGrades.push('E')
    }
  })
  return finalGrades
}

console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5])) //==> ['A+', 'B', 'C-', 'C', 'A-']

// the function is working correctly as per the requirement.

```

















































































































