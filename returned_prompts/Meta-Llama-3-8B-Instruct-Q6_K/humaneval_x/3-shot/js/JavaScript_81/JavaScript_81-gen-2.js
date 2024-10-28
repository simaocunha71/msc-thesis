  let letterGrades = [];
  for (const grade of grades) {
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
  }
  return letterGrades;
}
// Example usage:
console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5])); // Output: ['A+', 'B', 'C-', 'C', 'A-']



