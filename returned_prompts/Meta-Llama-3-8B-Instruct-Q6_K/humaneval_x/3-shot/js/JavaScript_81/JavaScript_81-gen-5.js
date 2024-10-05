  let letter_grades = [];
  grades.forEach((gpa) => {
    if (gpa >= 4.0) {
      letter_grades.push('A+');
    } else if (gpa > 3.7) {
      letter_grades.push('A');
    } else if (gpa > 3.3) {
      letter_grades.push('A-');
    } else if (gpa > 3.0) {
      letter_grades.push('B+');
    } else if (gpa > 2.7) {
      letter_grades.push('B');
    } else if (gpa > 2.3) {
      letter_grades.push('B-');
    } else if (gpa > 2.0) {
      letter_grades.push('C+');
    } else if (gpa > 1.7) {
      letter_grades.push('C');
    } else if (gpa > 1.3) {
      letter_grades.push('C-');
    } else if (gpa > 1.0) {
      letter_grades.push('D+');
    } else if (gpa > 0.7) {
      letter_grades.push('D');
    } else if (gpa > 0.0) {
      letter_grades.push('D-');
    } else {
      letter_grades.push('E');
    }
  });
  return letter_grades;
}
// Example usage:
console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5])); // Output: ["A+", "B", "C-", "C", "A-"]



