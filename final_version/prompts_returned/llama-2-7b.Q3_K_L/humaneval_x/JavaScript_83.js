/*
  Given a positive integer n, return the count of the numbers of n-digit
  positive integers that start or end with 1.
  */
const startsOneEnds = (n) => {
  let oneCount = 0;
  for(let i = n -1 ; i >= 1 ; i-- ) {
    if( i % 10 === 1 && i !== 1 ) {
      oneCount++;
    }
  }
  return oneCount;
}