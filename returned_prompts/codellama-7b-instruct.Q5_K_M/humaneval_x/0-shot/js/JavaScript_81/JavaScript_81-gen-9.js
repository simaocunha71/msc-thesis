/*It is the last week of the semester and the teacher has to give the grades
  to students. The teacher has been making her own algorithm for grading.
  The only problem is, she has lost the code she used for grading.
  She has given you a list of GPAs for some students and you have to write
  a function that can output a list of letter grades using the following table:
           GPA       |    Letter grade
            4.0                A+
          > 3.7                A
          > 3.3                A-
          > 3.0                B+
          > 2.7                B
          > 2.3                B-
          > 2.0                C+
          > 1.7                C
          > 1.3                C-
          > 1.0                D+
          > 0.7                D
          > 0.0                D-
            0.0                E


  Example:
  numericalLetterGrade([4.0, 3, 1.7, 2, 3.5]) ==> ['A+', 'B', 'C-', 'C', 'A-']
  */


const numericalLetterGrade = (grades) => {
  const result = [];
  for (let i = 0; i < grades.length; i++) {
    if (grades[i] >= 4.0) {
      result.push('A+');
    } else if (grades[i] >= 3.7) {
      result.push('A');
    } else if (grades[i] >= 3.3) {
      result.push('A-');
    } else if (grades[i] >= 3.0) {
      result.push('B+');
    } else if (grades[i] >= 2.7) {
      result.push('B');
    } else if (grades[i] >= 2.3) {
      result.push('B-');
    } else if (grades[i] >= 2.0) {
      result.push('C+');
    } else if (gr