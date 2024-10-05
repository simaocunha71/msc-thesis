Here is a JavaScript function that implements the algorithm described:
```
const numericalLetterGrade = (grades) => {
  return grades.map(gpa => {
    if (gpa >= 4.0) return 'A+';
    if (gpa > 3.7) return 'A';
    if (gpa > 3.3) return 'A-';
    if (gpa > 3.0) return 'B+';
    if (gpa > 2.7) return 'B';
    if (gpa > 2.3) return 'B-';
    if (gpa > 2.0) return 'C+';
    if (gpa > 1.7) return 'C';
    if (gpa > 1.3) return 'C-';
    if (gpa > 1.0) return 'D+';
    if (gpa > 0.7) return 'D';
    if (gpa > 0.0) return 'D-';
    return 'E';
  });
};
```
Here's an explanation of how the function works:

1. The function takes an array of GPAs as input.
2. It uses the `map()` method to iterate over the array of GPAs.
3. For each GPA, it checks if the GPA is greater than or equal to a certain threshold.
4. If the GPA is greater than or equal to the threshold, it returns the corresponding letter grade.
5. If the GPA is less than the threshold, it continues to the next threshold until it finds a match.
6. If the GPA is less than 0.0, it returns the letter grade 'E'.
7. The `map()` method returns a new array with the letter grades corresponding to each GPA in the original array.

You can test the function with the example input provided:
```
console.log(numericalLetterGrade([4.0, 3, 1.7, 2, 3.5])); // Output: ['A+', 'B', 'C-', 'C', 'A-']
```A: This is a JavaScript function that takes an array of GPAs as input and returns an array of letter grades based on the provided table. It uses the `map()` method to iterate over the array of GPAs and checks if each GPA is greater than or equal to a certain threshold. If the GPA is greater than or equal to the threshold,