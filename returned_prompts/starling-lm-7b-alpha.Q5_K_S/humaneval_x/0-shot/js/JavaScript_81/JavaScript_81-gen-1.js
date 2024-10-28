// Here is my solution:

function numericalLetterGrade(grades) {
  const gradeLetter = {
    Aplus: 4.0,
    A: 3.7,
    Aminus: 3.3,
    Bplus: 3.0,
    B: 2.7,
    Bminus: 2.3,
    Cplus: 2.0,
    C: 1.7,
    Cminus: 1.3,
    Dplus: 1.0,
    D: 0.7,
    Dminus: 0.0,
    E: 0.0
  };

  let result = [];

  for (let grade of grades) {
    for (let key in gradeLetter) {
      if (grade <= gradeLetter[key]) {
        result.push(key);
        break;
      }
    }
  }

  return result;
}

console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5])); // ['A+', 'B', 'C-', 'C', 'A-']

};

numericalLetterGrade([4.0, 3, 1.7, 2, 3.5]); // ['A+', 'B', 'C-', 'C', 'A-']

*/




















































































































































































