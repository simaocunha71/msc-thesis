
const largestSmallestIntegers = (lst) => {
  let largestNegative = null;
  let smallestPositive = null;

  for(let i = 0; i < lst.length; i++) {
    if(lst[i] < 0) {
      if(largestNegative === null || largestNegative < lst[i]) {
        largestNegative = lst[i];
      }
    }
    if(lst[i] > 0) {
      if(smallestPositive === null || smallestPositive > lst[i]) {
        smallestPositive = lst[i];
      }
    }
  }

  return [largestNegative, smallestPositive];
}

const lst = [2, 4, 1, 3, 5, 7];
console.log(largestSmallestIntegers(lst));

B:

const largestSmallestIntegers = (lst) => {
  let largestNegative = null;
  let smallestPositive = null;

  for(let i = 0; i < lst.length; i++) {
    if(lst[i] < 0) {
      if(largestNegative === null || largestNegative < lst[i]) {
        largestNegative = lst[i];
      }
    }
    if(lst[i] > 0) {
      if(smallestPositive === null || smallestPositive > lst[i]) {
        smallestPositive = lst[i];
      }
    }
  }

  return [largestNegative, smallestPositive];
}

const lst = [1, 2, 3, 4, 5];
console.log(largestSmallestIntegers(lst));

C:

const largestSmallestIntegers = (lst) => {
  let largestNegative = null;
  let smallestPositive = null;

  for(let i = 0; i < lst.length; i++) {
    if(lst[i] < 0) {
      if(largestNegative ===