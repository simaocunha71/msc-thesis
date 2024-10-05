const gradeMap = {
  4: "A+",
  3.7: "A",
  3.3: "A-",
  3: "B+",
  2.7: "B",
  2.3: "B-",
  2: "C+",
  1.7: "C",
  1.3: "C-",
  1: "D+",
  0.7: "D",
  0: "D-",
  0.0: "E"
};

return grades.map(grade => {
  for (const key in gradeMap) {
    if (grade >= parseFloat(key)) {
      return gradeMap[key];
    }
  }
});

};

module.exports = numericalLetterGrade;

/*
  The above code is incorrect because:

  The code does not use the correct data structure to represent a range of grades.
  The code does not convert the grades to the correct data type.
  The code does not use a for loop to check if a grade is in a range.
  The code does not use a function to determine the letter grade for a given GPA.

  Correction:

  First, create a hash map to represent the range of grades and the corresponding letter grades.
  Next, convert the grades to the correct data type.
  Then, use a for loop to check if a grade is in a range and use the correct function to determine the letter grade.


  The corrected code is:

  const numericalLetterGrade = (grades) => {
  const gradeMap = {
    4: "A+",
    3.7: "A",
    3.3: "A-",
    3: "B+",
    2.7: "B",
    2.3: "B-",
    2: "C+",
    1.7: "C",
    1.3: "C-",
    1: "D+",
    0.7: "D",
    0: "D-",
    0.0: "E"
  };

  return grades.map(grade => {
    for (const key in gradeMap) {
