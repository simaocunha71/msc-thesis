  const letter_grades = [
    [4.0, 'A+'],
    [3.7, 'A'],
    [3.3, 'A-'],
    [3.0, 'B+'],
    [2.7, 'B'],
    [2.3, 'B-'],
    [2.0, 'C+'],
    [1.7, 'C'],
    [1.3, 'C-'],
    [1.0, 'D+'],
    [0.7, 'D'],
    [0.0, 'D-'],
    [-0.7, 'E'],
    [-1.0, 'F'],
    [-1.3, 'F'],
    [-1.7, 'F'],
    [-2.0, 'F'],
    [-2.3, 'F'],
    [-2.7, 'F'],
    [-3.0, 'F'],
    [-3.3, 'F'],
    [-3.7, 'F'],
    [-4.0, 'F'],
  ];

  return grades.map(grade => {
    for (const [gpa, letter_grade] of letter_grades) {
      if (grade >= gpa) {
        return letter_grade;
      }
    }
  });
}



