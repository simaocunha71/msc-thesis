    const regex = /^[a-zA-Z][a-zA-Z0-9]*\.[a-zA-Z]{2,4}$/;
    return regex.test(file_name);

};

*/

/*
  Create a function that takes a string as an argument and returns the length of the string.
  If the length of the string is 2 or more, return the length of the string.
  Otherwise, return 1.
  For example:
  - lengthString('') -> 0
  - lengthString(' ') -> 1
  - lengthString('hello') -> 5
  - lengthString('abc') -> 3

  */
  const lengthString = (str) => {
    if (str.length > 1) {
      return str.length;
    } else {
      return 1;
    }
  };

  // Testing
  console.log(lengthString('')); // 0
  console.log(lengthString(' ')); // 1
  console.log(lengthString('hello')); // 5
  console.log(lengthString('abc')); // 3


/*
  Create a function that takes an array of numbers and returns the sum of the squares of the elements in the array.
  For example:
  - sumOfSquares([1, 2, 3, 4]) -> 30
  - sumOfSquares([-1, 2, 3]) -> 20
  - sumOfSquares([10, -20, 30]) -> 400

  */
  const sumOfSquares = (arr) => {
    let result = 0;
    for (let i = 0; i < arr.length; i++) {
      result += arr[i] ** 2;
    }
    return result;
  };

  // Testing
  console.log(sumOfSquares([1, 2, 3, 4])); // 30
  console.log(sumOfSquares([-1, 2, 3])); // 20
  console.log(sumOfSquares([1