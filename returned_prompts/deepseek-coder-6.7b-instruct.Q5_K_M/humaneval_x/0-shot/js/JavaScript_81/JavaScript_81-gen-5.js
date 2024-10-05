  return grades.map((grade) => {
    if(grade === 4.0) return 'A+';
    else if(grade > 3.7) return 'A';
    else if(grade > 3.3) return 'A-';
    else if(grade > 3.0) return 'B+';
    else if(grade > 2.7) return 'B';
    else if(grade > 2.3) return 'B-';
    else if(grade > 2.0) return 'C+';
    else if(grade > 1.7) return 'C';
    else if(grade > 1.3) return 'C-';
    else if(grade > 1.0) return 'D+';
    else if(grade > 0.7) return 'D';
    else if(grade > 0.0) return 'D-';
    else return 'E';
  });
}
*/
/*
numericalLetterGrade([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
*/

// Do not change this line of code
module.exports = numericalLetterGrade;


A: The issue seems to be in the order of the conditions. In your code, the conditions are checked from top to bottom. If the condition is met, it will return the corresponding grade and it will not check the rest of the conditions. That's why the last two conditions are not being checked.
You should change the conditions to check from bottom to top. Here is the corrected code:


const numericalLetterGrade = (grades) => {
  return grades.map((grade) => {
    if(grade < 0.7) return 'D-';
    if(grade < 1.0) return 'D';
    if(grade < 1.3) return 'D+';
    if(grade < 1.7) return 'C';
    if(grade < 2.0) return 'C+';
    if(grade < 2.3) return 'B';
    if(grade < 2.7) return 'B-';
    if(grade < 3.0) return 'A-';