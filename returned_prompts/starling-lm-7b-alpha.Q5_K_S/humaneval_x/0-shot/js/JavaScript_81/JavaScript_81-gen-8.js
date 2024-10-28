let gradesList = [];

for(let i = 0; i < grades.length; i++) {
  if(grades[i] >= 4.0) {
    gradesList.push('A+');
  } else if(grades[i] >= 3.7) {
    gradesList.push('A');
  } else if(grades[i] >= 3.3) {
    gradesList.push('A-');
  } else if(grades[i] >= 3.0) {
    gradesList.push('B+');
  } else if(grades[i] >= 2.7) {
    gradesList.push('B');
  } else if(grades[i] >= 2.3) {
    gradesList.push('B-');
  } else if(grades[i] >= 2.0) {
    gradesList.push('C+');
  } else if(grades[i] >= 1.7) {
    gradesList.push('C');
  } else if(grades[i] >= 1.3) {
    gradesList.push('C-');
  } else if(grades[i] >= 1.0) {
    gradesList.push('D+');
  } else if(grades[i] >= 0.7) {
    gradesList.push('D');
  } else if(grades[i] >= 0.0) {
    gradesList.push('D-');
  } else {
    gradesList.push('E');
  }
}

return gradesList;
};







module.exports = numericalLetterGrade;




























































































































