  const numericalLetterGrade = (grades) => {
    const gpa = grades.filter(grade => grade >= 0 && grade <= 4.0);
    if (gpa.length === 0) {
      return 'E';
    }
    if (gpa >= 4.0) {
      return 'A+';
    }
    if (gpa >= 3.7) {
      return 'A';
    }
    if (gpa >= 3.3) {
      return 'A-';
    }
    if (gpa >= 3.0) {
      return 'B+';
    }
    if (gpa >= 2.7) {
      return 'B';
    }
    if (gpa >= 2.3) {
      return 'B-';
    }
    if (gpa >= 2.0) {
      return 'C+';
    }
    if (gpa >= 1.7) {
      return 'C';
    }
    if (gpa >= 1.3) {
      return 'C-';
    }
    if (gpa >= 1.0) {
      return 'D+';
    }
    if (gpa >= 0.7) {
      return 'D';
    }
    return 'E';
  };

  // console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5]));

  // const numericalLetterGrade = (grades) => {
  //   const gpa = grades.filter(grade => grade >= 0 && grade <= 4.0);
  //   if (gpa.length === 0) {
  //     return 'E';
  //   }
  //   if (gpa >= 4.0) {
  //     return 'A+';
  //   }
  //   if (gpa >= 3.7) {
  //     return 'A';
  //   }
  //   if (gpa >= 3.3) {
  //     return 'A-';
  //  