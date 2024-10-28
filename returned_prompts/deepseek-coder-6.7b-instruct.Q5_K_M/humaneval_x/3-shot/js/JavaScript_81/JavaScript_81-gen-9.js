  return grades.map(grade => {
    if (grade == 4.0) return 'A+';
    if (grade > 3.7) return 'A';
    if (grade > 3.3) return 'A-';
    if (grade > 3.0) return 'B+';
    if (grade > 2.7) return 'B';
    if (grade > 2.3) return 'B-';
    if (grade > 2.0) return 'C+';
    if (grade > 1.7) return 'C';
    if (grade > 1.3) return 'C-';
    if (grade > 1.0) return 'D+';
    if (grade > 0.7) return 'D';
    if (grade > 0.0) return 'D-';
    return 'E';
  });
}



