  const letter_grades = [];

  for (const g of grades) {
    if (g == 4.0) {
      letter_grades.push('A+');
    } else if (g > 3.7) {
      letter_grades.push('A');
    } else if (g > 3.3) {
      letter_grades.push('A-');
    } else if (g > 3.0) {
      letter_grades.push('B+');
    } else if (g > 2.7) {
      letter_grades.push('B');
    } else if (g > 2.3) {
      letter_grades.push('B-');
    } else if (g > 2.0) {
      letter_grades.push('C+');
    } else if (g > 1.7) {
      letter_grades.push('C');
    } else if (g > 1.3) {
      letter_grades.push('C-');
    } else if (g > 1.0) {
      letter_grades.push('D+');
    } else if (g > 0.7) {
      letter_grades.push('D');
    } else if (g > 0.0) {
      letter_grades.push('D-');
    } else if (g == 0.0) {
      letter_grades.push('E');
    }
  }

  return letter_grades;
}


