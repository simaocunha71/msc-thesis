  let letterGrades = []

  grades.forEach(grade => {
    if (grade === 4.0) letterGrades.push('A+')
    else if (grade > 3.7) letterGrades.push('A')
    else if (grade > 3.3) letterGrades.push('A-')
    else if (grade > 3.0) letterGrades.push('B+')
    else if (grade > 2.7) letterGrades.push('B')
    else if (grade > 2.3) letterGrades.push('B-')
    else if (grade > 2.0) letterGrades.push('C+')
    else if (grade > 1.7) letterGrades.push('C')
    else if (grade > 1.3) letterGrades.push('C-')
    else if (grade > 1.0) letterGrades.push('D+')
    else if (grade > 0.7) letterGrades.push('D')
    else if (grade > 0.0) letterGrades.push('D-')
    else letterGrades.push('E')
  })

  return letterGrades
}

console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5])) // ['A+', 'B', 'C-', 'C', 'A-']

This solution is straightforward, it will iterate over each grade and compare it with the conditions given in the problem statement. Based on the conditions, it will push the corresponding letter grade into the `letterGrades` array. Finally, it will return the `letterGrades` array.

*/

const numericalLetterGrade = (grades) => {
  let letterGrades = []

  grades.forEach(grade => {
    switch(true) {
      case grade === 4.0:
        letterGrades.push('A+')
        break
      case grade > 3.7:
        letterGrades.push('A')
        break
      case grade > 3.3:
        letterGrades.push('A-')
        break
      case grade > 3.0:
        letterGrades