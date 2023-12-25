/*
  pairsSumToZero takes a list of integers as an input.
  it returns true if there are two distinct elements in the list that
  sum to zero, and false otherwise.
  >>> pairsSumToZero([1, 3, 5, 0])
  false
  >>> pairsSumToZero([1, 3, -2, 1])
  false
  >>> pairsSumToZero([1, 2, 3, 7])
  false
  >>> pairsSumToZero([2, 4, -5, 3, 5, 7])
  true
  >>> pairsSumToZero([1])
  false
  */
const pairsSumToZero = (l) => {
  let n = l.length;
  if (!n) return false; // n=0
  const m = 2 * n - l.reduce((a, b) => a + b);
  if ((m % 2) === 1) return true; // if there are two nonzeroes, we found one of them
  for (let i = 0; i < l.length / 2; i++) {
    const j = i + n;
    let val1 = l[i];
    let val2 = l[j]
    if ((val1 === undefined) || (val2 === undefined)) return false; // one of them is undefined, it's not a pair
    if (val1 < 0 && val2 > 0) { // or they cancel eachother out
      continue;
    } else if (val1 > 0 && val2 < 0) { // another way to say the same thing: 
      continue;
    } else if (!(val1 % 2 === 1)) { return false;}// val1 is not a multiple of 2 and its 2'd power  is not a multiple of it either, so we found one
    let r = (l[j] * l[i]) / Math.pow(val1, val2);
    // console.log('r:' + r)
    if (!r && !isNaN(r)) return false;// found a second element that is not 0 and not -0
    let temp = r < 0 ? -