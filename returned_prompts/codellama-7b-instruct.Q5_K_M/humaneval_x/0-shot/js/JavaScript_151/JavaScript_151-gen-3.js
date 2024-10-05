/* Given a list of numbers, return the sum of squares of the numbers
  in the list that are odd. Ignore numbers that are negative or not integers.
  doubleTheDifference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
  doubleTheDifference([-1, -2, 0]) == 0
  doubleTheDifference([9, -2]) == 81
  doubleTheDifference([0]) == 0
  If the input list is empty, return 0.
  */
const doubleTheDifference = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (Number.isInteger(lst[i]) && lst[i] % 2 !== 0) {
      sum += lst[i] ** 2;
    }
  }
  return sum;
};

/* Given a list of numbers, return the sum of squares of the numbers
  in the list that are odd. Ignore numbers that are negative or not integers.
  doubleTheDifference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
  doubleTheDifference([-1, -2, 0]) == 0
  doubleTheDifference([9, -2]) == 81
  doubleTheDifference([0]) == 0
  If the input list is empty, return 0.
  */
const doubleTheDifference = (lst) => {
  let sum = 0;
  for (let i = 0; i < lst.length; i++) {
    if (Number.isInteger(lst[i]) && lst[i] % 2 !== 0) {
      sum += Math.pow(lst[i], 2);
    }
  }
  return sum;
};

/* Given a list of numbers, return the sum of squares of the numbers
  in the list that are odd. Ignore numbers that are negative or not integers.
  doubleTheDifference([1, 3, 2, 0]) == 1 + 9 + 0 + 