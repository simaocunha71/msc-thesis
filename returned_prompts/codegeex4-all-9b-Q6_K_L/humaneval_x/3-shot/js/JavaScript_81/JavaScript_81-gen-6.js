  return grades.map(x => {
    if (x >= 4.0) return 'A+';
    if (x >= 3.7) return 'A';
    if (x >= 3.3) return 'A-';
    if (x >= 3.0) return 'B+';
    if (x >= 2.7) return 'B';
    if (x >= 2.3) return 'B-';
    if (x >= 2.0) return 'C+';
    if (x >= 1.7) return 'C';
    if (x >= 1.3) return 'C-';
    if (x >= 1.0) return 'D+';
    if (x >= 0.7) return 'D';
    if (x >= 0.0) return 'D-';
    if (x == 0.0) return 'E';
  });
}



