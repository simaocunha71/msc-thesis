/*
  You are given a function, which takes a number as input, and returns a function as output.
  The output function takes a string as input, and returns the result of concatenating the input
  string with the input number.
  Examples:
      const double = makeAdder(2);
      double("hello") == "hello2";
      const triple = makeAdder(3);
      triple("world") == "world3";
  */
const makeAdder = (num) => (str) => str + num;

B:
/*
  You are given a function, which takes a number as input, and returns a function as output.
  The output function takes an array as input, and returns a new array where every element is
  the result of adding the input number to that element.
  Examples:
      const addTwo = makeAdderArray(2);
      addTwo([1, 2, 3]) == [3, 4, 5];
      const addThree = makeAdderArray(3);
      addThree([1, 2, 3]) == [4, 5, 6];
  */
const makeAdderArray = (num) => (arr) => arr.map((el) => el + num);

C:
/*
  You are given a function, which takes a number as input, and returns a function as output.
  The output function takes an object as input, and returns a new object where every property is
  the result of adding the input number to that property.
  Examples:
      const addTwo = makeAdderObject(2);
      addTwo({ a: 1, b: 2, c: 3 }) == { a: 3, b: 4, c: 5 };
      const addThree = makeAdderObject(3);
      addThree({ a: 1, b: 2, c: 3 }) == { a: 4, b: 5, c: 6 };
  */
const makeAdderObject = (num) => (obj) =>
  Object.keys(obj).reduce((acc, key) => ({ ...acc, [key]: obj[key] + num }), {});

D:
/*
 