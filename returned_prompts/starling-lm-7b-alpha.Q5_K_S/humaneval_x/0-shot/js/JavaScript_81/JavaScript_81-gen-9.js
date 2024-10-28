
let result = [];

grades.forEach((grade) => {
  if (grade > 0.0 && grade <= 1.0) {
    result.push('D+');
  } else if (grade > 1.0 && grade <= 1.3) {
    result.push('D');
  } else if (grade > 1.3 && grade <= 1.7) {
    result.push('C-');
  } else if (grade > 1.7 && grade <= 2.0) {
    result.push('C');
  } else if (grade > 2.0 && grade <= 2.3) {
    result.push('B-');
  } else if (grade > 2.3 && grade <= 2.7) {
    result.push('B');
  } else if (grade > 2.7 && grade <= 3.0) {
    result.push('B+');
  } else if (grade > 3.0 && grade <= 3.3) {
    result.push('A-');
  } else if (grade > 3.3 && grade <= 3.7) {
    result.push('A');
  } else if (grade > 3.7 && grade <= 4.0) {
    result.push('A+');
  }
});

return result;

};





























































































































































































