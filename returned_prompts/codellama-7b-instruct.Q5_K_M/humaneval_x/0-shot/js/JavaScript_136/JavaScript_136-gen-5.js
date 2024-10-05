const largestSmallestIntegers = (lst) => {
  // return [null, null] if lst is empty
  if (!lst || !lst.length) return [null, null];

  // initialize variables
  let largestNeg = null;
  let smallestPos = null;

  // loop through the list
  for (let i = 0; i < lst.length; i++) {
    // check if the current element is a negative integer
    if (lst[i] < 0) {
      // if the current element is a negative integer and it's
      // smaller than the current largest negative integer
      // update the largest negative integer
      if (lst[i] < largestNeg) {
        largestNeg = lst[i];
      }
    } else {
      // if the current element is a positive integer and it's
      // larger than the current smallest positive integer
      // update the smallest positive integer
      if (lst[i] > smallestPos) {
        smallestPos = lst[i];
      }
    }
  }

  // return the list [largestNeg, smallestPos]
  return [largestNeg, smallestPos];
};


const largestSmallestIntegers = (lst) => {
  let largestNeg = null;
  let smallestPos = null;
  for (let i = 0; i < lst.length; i++) {
    if (lst[i] < 0) {
      if (lst[i] < largestNeg || largestNeg === null) {
        largestNeg = lst[i];
      }
    } else if (lst[i] > 0) {
      if (lst[i] < smallestPos || smallestPos === null) {
        smallestPos = lst[i];
      }
    }
  }
  return [largestNeg, smallestPos];
};
