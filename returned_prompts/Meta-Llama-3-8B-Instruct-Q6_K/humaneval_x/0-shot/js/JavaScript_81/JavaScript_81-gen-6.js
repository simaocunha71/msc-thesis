```javascript
const numericalLetterGrade = (grades) => {
  return grades.map((gpa) => {
    if (gpa >= 4.0) return 'A+';
    if (gpa >= 3.7) return 'A';
    if (gpa >= 3.3) return 'A-';
    if (gpa >= 3.0) return 'B+';
    if (gpa >= 2.7) return 'B';
    if (gpa >= 2.3) return 'B-';
    if (gpa >= 2.0) return 'C+';
    if (gpa >= 1.7) return 'C';
    if (gpa >= 1.3) return 'C-';
    if (gpa >= 1.0) return 'D+';
    if (gpa >= 0.7) return 'D';
    if (gpa >= 0.0) return 'D-';
    return 'E';
  });
};
```


Explanation:
This function takes an array of GPAs as input and returns an array of letter grades. It uses the `map()` function to iterate over each GPA in the input array and applies the grading rules to each GPA. The function checks for each GPA if it is greater than or equal to the specified GPA range for a particular letter grade, and returns the corresponding letter grade. If the GPA does not fall within any of the specified ranges, it returns 'E'. The function returns an array of letter grades that correspond to the input GPAs.