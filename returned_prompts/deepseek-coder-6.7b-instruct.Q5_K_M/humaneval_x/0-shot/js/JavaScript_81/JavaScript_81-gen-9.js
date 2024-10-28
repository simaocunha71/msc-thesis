  let letterGrades = [];
  for (let i = 0; i < grades.length; i++) {
    if (grades[i] === 4.0) letterGrades.push('A+');
    else if (grades[i] > 3.7) letterGrades.push('A');
    else if (grades[i] > 3.3) letterGrades.push('A-');
    else if (grades[i] > 3.0) letterGrades.push('B+');
    else if (grades[i] > 2.7) letterGrades.push('B');
    else if (grades[i] > 2.3) letterGrades.push('B-');
    else if (grades[i] > 2.0) letterGrades.push('C+');
    else if (grades[i] > 1.7) letterGrades.push('C');
    else if (grades[i] > 1.3) letterGrades.push('C-');
    else if (grades[i] > 1.0) letterGrades.push('D+');
    else if (grades[i] > 0.7) letterGrades.push('D');
    else if (grades[i] > 0.0) letterGrades.push('D-');
    else letterGrades.push('E');
  }
  return letterGrades;
}

console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5]));
//Expected output: ['A+', 'B', 'C-', 'C', 'A-']
```

The function `numericalLetterGrade` takes an array of GPAs as input and returns an array of equivalent letter grades based on the provided grading scale.

The function uses a for loop to iterate through the input grades array, and a series of if-else statements to determine the corresponding letter grade for each GPA.

The letter grades are then pushed into the `letterGrades` array, which is returned at the end of the function.

The output of the `numericalLetterGrade` function for the provided input `[4.0, 3, 1.7, 