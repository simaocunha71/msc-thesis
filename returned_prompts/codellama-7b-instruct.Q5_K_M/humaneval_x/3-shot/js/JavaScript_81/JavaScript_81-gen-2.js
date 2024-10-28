  var letter_grades = ['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D', 'D-', 'E'];

  return grades.map(function(gpa) {
    var index = Math.floor(gpa * (letter_grades.length - 1));
    return letter_grades[index];
  });
}



