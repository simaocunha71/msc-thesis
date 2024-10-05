  var letter_grades = [];
  var letter_grade;
  for (let i = 0; i < grades.length; i++) {
    if (grades[i] == 4.0) {
      letter_grade = 'A+';
    } else if (grades[i] > 3.7) {
      letter_grade = 'A';
    } else if (grades[i] > 3.3) {
      letter_grade = 'A-';
    } else if (grades[i] > 3.0) {
      letter_grade = 'B+';
    } else if (grades[i] > 2.7) {
      letter_grade = 'B';
    } else if (grades[i] > 2.3) {
      letter_grade = 'B-';
    } else if (grades[i] > 2.0) {
      letter_grade = 'C+';
    } else if (grades[i] > 1.7) {
      letter_grade = 'C';
    } else if (grades[i] > 1.3) {
      letter_grade = 'C-';
    } else if (grades[i] > 1.0) {
      letter_grade = 'D+';
    } else if (grades[i] > 0.7) {
      letter_grade = 'D';
    } else if (grades[i] > 0.0) {
      letter_grade = 'D-';
    } else {
      letter_grade = 'E';
    }
    letter_grades.push(letter_grade);
  }
  return letter_grades;
}