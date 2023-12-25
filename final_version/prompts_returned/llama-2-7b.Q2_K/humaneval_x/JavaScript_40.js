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
  let total = 0;
  for(let i = 0 ;i < l.length; i++){
    let sum = 0
    for(let j=0;j<l.length;j++){
      if(j == i){continue;}
      else{sum += l[j];}
    }
   if(total == 0 && sum == 0){return true}
  }
  return false;
};
