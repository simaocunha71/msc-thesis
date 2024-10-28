    let arr = [];
    arr.push(a * a + b * b === c * c);
    arr.push(a * a + c * c === b * b);
    arr.push(b * b + c * c === a * a);

    return arr.some(x => x === true);
};

/*
 Given an array of integers, find the sum of all the integers.
  Return the sum.
  Example:
  sumArray([1, 2, 3, 4]) == 10
  sumArray([-1, 2, -3, 4]) == 6
  sumArray([]) == 0
  */
const sumArray = (arr) => {
    return arr.reduce((a, b) => a + b, 0);
};

/*
 Given an array of integers, return a new array with all the integers
  multiplied by 2.
  Example:
  doubleArray([1, 2, 3, 4]) == [2, 4, 6, 8]
  doubleArray([]) == []
  */
const doubleArray = (arr) => {
    return arr.map(x => x * 2);
};

/*
 Given an array of integers, return a new array with all the odd numbers.
  Example:
  oddArray([1, 2, 3, 4, 5]) == [1, 3, 5]
  oddArray([]) == []
  */
const oddArray = (arr) => {
    return arr.filter(x => x % 2 !== 0);
};

/*
 Given an array of integers, return a new array with all the even numbers.
  Example:
  evenArray([1, 2, 3, 4, 5]) == [2, 4]
  evenArray([]) == []
  */
const evenArray = (arr) => {
    return arr.filter(x => x % 2 === 0);
};

/*
 Given an array of integers, return a new array with all the elements
  sorted in ascending order.
  Example:
  ascendingOrderArray([1, 