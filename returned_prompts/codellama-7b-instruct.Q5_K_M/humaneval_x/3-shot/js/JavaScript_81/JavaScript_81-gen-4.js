  var result = [];
  var letter_grade = '';

  for (let grade of grades) {
    if (grade >= 4.0) {
      letter_grade = 'A+';
    } else if (grade >= 3.7) {
      letter_grade = 'A';
    } else if (grade >= 3.3) {
      letter_grade = 'A-';
    } else if (grade >= 3.0) {
      letter_grade = 'B+';
    } else if (grade >= 2.7) {
      letter_grade = 'B';
    } else if (grade >= 2.3) {
      letter_grade = 'B-';
    } else if (grade >= 2.0) {
      letter_grade = 'C+';
    } else if (grade >= 1.7) {
      letter_grade = 'C';
    } else if (grade >= 1.3) {
      letter_grade = 'C-';
    } else if (grade >= 1.0) {
      letter_grade = 'D+';
    } else if (grade >= 0.7) {
      letter_grade = 'D';
    } else if (grade >= 0.0) {
      letter_grade = 'D-';
    } else {
      letter_grade = 'E';
    }
    result.push(letter_grade);
  }

  return result;
}



