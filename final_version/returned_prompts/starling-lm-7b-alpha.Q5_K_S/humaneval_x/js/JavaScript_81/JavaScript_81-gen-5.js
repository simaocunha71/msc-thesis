  const gradesToLetters = [
    { gpa: 4.0, letter: 'A+' },
    { gpa: 3.7, letter: 'A' },
    { gpa: 3.3, letter: 'A-' },
    { gpa: 3.0, letter: 'B+' },
    { gpa: 2.7, letter: 'B' },
    { gpa: 2.3, letter: 'B-' },
    { gpa: 2.0, letter: 'C+' },
    { gpa: 1.7, letter: 'C' },
    { gpa: 1.3, letter: 'C-' },
    { gpa: 1.0, letter: 'D+' },
    { gpa: 0.7, letter: 'D' },
    { gpa: 0.0, letter: 'D-' },
    { gpa: 0.0, letter: 'E' },
  ];

  return grades.map(grade => {
    for (const letter of gradesToLetters) {
      if (grade <= letter.gpa) {
        return letter.letter;
      }
    }
  });
}



