/*
  triplesSumToZero takes a list of integers as an input.
  it returns true if there are three distinct elements in the list that
  sum to zero, and false otherwise.

  >>> triplesSumToZero([1, 3, 5, 0])
  false
  >>> triplesSumToZero([1, 3, -2, 1])
  true
  >>> triplesSumToZero([1, 2, 3, 7])
  false
  >>> triplesSumToZero([2, 4, -5, 3, 9, 7])
  true
  >>> triplesSumToZero([1])
  false
  */
const triplesSumToZero = (l) => {
  let result = false;
  for(let i=0; i< l.length-2; i++){
    if (l[i] + l[i+1] - l[i+2]) === 0 && l[i] != 0 && l[i+1] != 0 && l[i+2]!=0){
      result = true;
    }else {
      return false
    }
  }
  return result;
}