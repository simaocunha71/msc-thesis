  return grades.map(gpa => {
      if (gpa === 4.0) return 'A+';
      if (gpa > 3.7) return 'A';
      if (gpa > 3.3) return 'A-';
      if (gpa > 3.0) return 'B+';
      if (gpa > 2.7) return 'B';
      if (gpa > 2.3) return 'B-';
      if (gpa > 2.0) return 'C+';
      if (gpa > 1.7) return 'C';
      if (gpa > 1.3) return 'C-';
      if (gpa > 1.0) return 'D+';
      if (gpa > 0.7) return 'D';
      if (gpa > 0.0) return 'D-';
      return 'E';
  });
}



