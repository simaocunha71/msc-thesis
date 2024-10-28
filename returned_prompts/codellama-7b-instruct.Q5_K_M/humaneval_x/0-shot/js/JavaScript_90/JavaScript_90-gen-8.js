/*
  You are given a list of integers.
  Write a function nextSmallest() that returns the 2nd smallest element of the list.
  Return null if there is no such element.
  
  nextSmallest([1, 2, 3, 4, 5]) == 2
  nextSmallest([5, 1, 4, 3, 2]) == 2
  nextSmallest([]) == null
  nextSmallest([1, 1]) == null
  */
const nextSmallest = (lst) => {
  let arr = lst.sort((a, b) => a - b);
  let length = arr.length;
  let secSmallest = null;
  let i = 1;

  while (i < length) {
    if (secSmallest == null) {
      secSmallest = arr[i];
    } else if (secSmallest != arr[i]) {
      break;
    }
    i++;
  }

  return secSmallest;
};

