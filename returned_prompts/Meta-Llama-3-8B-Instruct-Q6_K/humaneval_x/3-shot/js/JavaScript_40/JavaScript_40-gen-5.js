  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      for (let k = j + 1; k < l.length; k++) {
        if (l[i] + l[j] + l[k] === 0) {
          return true;
        }
      }
    }
  }
  return false;
} // end of function triplesSumToZero
// triplesSumToZero([1, 3, 5, 0]) false
// triplesSumToZero([1, 3, -2, 1]) true
// triplesSumToZero([1, 2, 3, 7]) false
// triplesSumToZero([2, 4, -5, 3, 9, 7]) true
// triplesSumToZero([1]) false
// triplesSumToZero([1, 2]) false
// triplesSumToZero([1, 2, 3]) false
// triplesSumToZero([1, 2, 3, 4]) false
// triplesSumToZero([1, 2, 3, 4, 5]) false
// triplesSumToZero([1, 2, 3, 4, 5, 6]) false
// triplesSumToZero([1, 2, 3, 4, 5, 6, 7]) false
// triplesSumToZero([1, 2, 3, 4, 5, 6, 7, 8]) false
// triplesSumToZero([1, 2, 3, 4, 5, 6, 7, 8, 9]) false
// triplesSumToZero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) false
// triplesSumToZero([-1, 1, 1]) false
// triplesSumToZero([-1, 1, 2]) false
// triplesSumToZero([-1, 1, 3]) false
// triplesSumToZero([-1, 1, 4]) false
// triplesSumToZero([-1, 1, 5]) false
// triplesSumToZero([-1, 1, 6]) false