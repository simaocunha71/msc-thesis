  const letter_grades = ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E"];
  const grade_boundaries = [4.0, 3.7, 3.3, 3.0, 2.7, 2.3, 2.0, 1.7, 1.3, 1.0, 0.7, 0.0, 0.0];

  let result = [];
  for (const grade of grades) {
    for (let i = 0; i < grade_boundaries.length; i++) {
      if (grade_boundaries[i] < grade && grade < grade_boundaries[i+1]) {
        result.push(letter_grades[i]);
        break;
      }
    }
  }

  return result;
}



