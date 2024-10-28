  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      if (l[i] + l[j] === 0) {
        return true;
      }
    }
  }
  return false;
} // end of pairsSumToZero function
// pairsSumToZero([1, 2, 3, 7]) false
// pairsSumToZero([2, 4, -5, 3, 5, 7]) true
// pairsSumToZero([1]) false
// pairsSumToZero([1,3,5,0]) false
// pairsSumToZero([1,3,-2,1]) false
// pairsSumToZero([1,2,3,7]) false
// pairsSumToZero([1,2,3,4]) false
// pairsSumToZero([2,4,-5,3,5,7]) true
// pairsSumToZero([1,2,3,-7]) true
// pairsSumToZero([1,2,3,4,5,6]) false
// pairsSumToZero([2,4,-5,3,5,7]) true
// pairsSumToZero([1,2,3,-7]) true
// pairsSumToZero([2,4,-5,3,5,7]) true
// pairsSumToZero([1,2,3,4,5,6]) false
// pairsSumToZero([2,4,-5,3,5,7]) true
// pairsSumToZero([1,2,3,-7]) true
// pairsSumToZero([2,4,-5,3,5,7]) true
// pairsSumToZero([1,2,3,4,5,6]) false
// pairsSumToZero([2,4,-5,3,5,7]) true
// pairsSumToZero([1,2,3,-7]) true
// pairsSumToZero([2,4,-5,3,5,7]) true
// pairsSumToZero([1,2,3,4,5,6]) false
// pairsSumToZero([2,4,-5,3,5,7]) true
// pairsSumToZero([1,2,3,-7]) true