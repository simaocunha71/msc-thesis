/*
  Write a function which sorts the given list of integers
  in ascending order according to the sum of their digits.
  Note: if there are several items with similar sum of their digits,
  order them based on their index in original list.

  For example:
  >>> orderByPoints([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
  >>> orderByPoints([]) == []
  */
const orderByPoints = (nums) => {
  const sortByPoints = (a, b) => {
    const aPoints = getPoints(a);
    const bPoints = getPoints(b);
    if (aPoints !== bPoints) {
      return aPoints - bPoints;
    }
    return a - b;
  };

  const getPoints = (n) => {
    const str = n.toString();
    let points = 0;
    for (let i = 0; i < str.length; i++) {
      points += +str[i];
    }
    return points;
  };

  return nums.slice().sort(sortByPoints);
};

console.log(orderByPoints([1, 11, -1, -11, -12]));
console.log(orderByPoints([]));

