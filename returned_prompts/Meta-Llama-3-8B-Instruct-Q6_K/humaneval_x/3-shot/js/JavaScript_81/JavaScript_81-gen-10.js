  let letter_grades = [];
  for (let grade of grades) {
    if (grade >= 4.0) {
      letter_grades.push('A+');
    } else if (grade >= 3.7) {
      letter_grades.push('A');
    } else if (grade >= 3.3) {
      letter_grades.push('A-');
    } else if (grade >= 3.0) {
      letter_grades.push('B+');
    } else if (grade >= 2.7) {
      letter_grades.push('B');
    } else if (grade >= 2.3) {
      letter_grades.push('B-');
    } else if (grade >= 2.0) {
      letter_grades.push('C+');
    } else if (grade >= 1.7) {
      letter_grades.push('C');
    } else if (grade >= 1.3) {
      letter_grades.push('C-');
    } else if (grade >= 1.0) {
      letter_grades.push('D+');
    } else if (grade >= 0.7) {
      letter_grades.push('D');
    } else if (grade >= 0.0) {
      letter_grades.push('D-');
    } else {
      letter_grades.push('E');
    }
  }
  return letter_grades;
}