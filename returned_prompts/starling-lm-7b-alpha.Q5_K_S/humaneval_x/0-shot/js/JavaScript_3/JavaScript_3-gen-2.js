    let balance = 0;
    for (let i = 0; i < operations.length; i++) {
        balance += operations[i];
        if (balance < 0) {
            return true;
        }
    }
    return false;
};

/*
You are given an array of positive integers. Your task is to return the sum of all integers of the array rounded up to the nearest integer. Here are some examples of this rounding rule: 3.4 rounds up to 4, -3.4 rounds down to -3, and 0.4 rounds up to 1. If the decimal part is less than or equal to 0.5 (like in the first and third example), you should round down. Otherwise, you should round up.
  >>> roundUp([3.4, 4.9, 0.4])
  [4, 5, 1]
  >>> roundUp([-3.4, -2.5, 0.4])
  [-4, -3, 1]
  >>> roundUp([0.4, 3.4, -3.4])
  [1, 4, -4]
  >>> roundUp([])
  []

*/
const roundUp = (arr) => {
    return arr.map(num => Math.round(num));
};

/*
Given an array of integers, your task is to remove all the negative integers from the array, and return the result. Here are some examples:
  >>> noNegatives([1, -2, 3, -4, 5])
  [1, 3, 5]
  >>> noNegatives([])
  []
  >>> noNegatives([-1, -2, -3])
  []
*/
const noNegatives = (arr) => {
    return arr.filter(num => num >= 0);
};

/*
You are given an array of strings. Your task is to return a new array that contains all the strings of the input array, but in reverse order. Here are some examples:
  >>> reverseArray(["Hello", "World"])
  ["World", "Hello"]
  >>> reverseArray([])
  []
  >>> reverseArray(["Hello