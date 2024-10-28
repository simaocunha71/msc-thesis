

const numericalLetterGrade = (grades) => {
  let letterGrades = [];
  grades.forEach(grade => {
    if (grade === 4.0) letterGrades.push('A+');
    else if (grade > 3.7) letterGrades.push('A');
    else if (grade > 3.3) letterGrades.push('A-');
    else if (grade > 3.0) letterGrades.push('B+');
    else if (grade > 2.7) letterGrades.push('B');
    else if (grade > 2.3) letterGrades.push('B-');
    else if (grade > 2.0) letterGrades.push('C+