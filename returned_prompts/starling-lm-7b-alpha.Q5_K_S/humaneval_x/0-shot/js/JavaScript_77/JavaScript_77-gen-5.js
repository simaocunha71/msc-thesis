return Math.cbrt(Math.pow(a, 3)) === a;
};


/*
  Write a function that takes an array of strings and returns true if all strings are equal to the first string.
  Examples:
  allEqual(["foo", "foo", "foo"]) ==> true
  allEqual(["foo", "bar", "baz"]) ==> false
  allEqual(["foo"]) ==> true
  allEqual([]) ==> false
  allEqual([null]) ==> true
  allEqual([123]) ==> false
  */

const allEqual = (strs) => {

B:
return strs.length === 0 || strs.every((str) => str === strs[0]);
};



/*
  Write a function that takes an array of numbers and returns a new array with all the numbers in the original array but with the numbers in reverse order.
  Examples:
  reverse([1, 2, 3, 4, 5]) ==> [5, 4, 3, 2, 1]
  reverse([]) ==> []
  reverse([1]) ==> [1]
  */

const reverse = (nums) => {

C:
return [...nums].reverse();
};


/*
  Write a function that takes an array of strings and returns a new array with all the strings in the original array but with the strings in reverse order.
  Examples:
  reverseString(["a", "b", "c"]) ==> ["c", "b", "a"]
  reverseString([]) ==> []
  reverseString(["1", "2", "3"]) ==> ["3", "2", "1"]
  reverseString(["foo", "bar", "baz"]) ==> ["baz", "bar", "foo"]
  */

const reverseString = (strs) => {

D:
return [...strs].reverse().map((str) => str);
};


/*
  Write a function that takes an array of numbers and returns the sum of all the numbers in the array.
  Examples:
  sum([1, 2, 3, 4, 5]) ==> 15
  sum([]) ==> 0
  sum