
const sumSquares = lst => {
  let result = 0;
  for (let i = 0; i < lst.length; i++) {
    if (i % 3 === 0) {
      result += Math.pow(lst[i], 2);
    }
    if (i % 4 === 0 && i % 3 !== 0) {
      result += Math.pow(lst[i], 3);
    }
  }
  return result;
};

//*
  Examples:
  for lst = [1,2,3] the output should be 6
  for lst = []  the output should be 0
  for lst = [-1,-5,2,-1,-5]  the output should be -126
  */
  const sumSquares = (lst) => {
    let result = 0;
    for (let i = 0; i < lst.length; i++) {
      if (i % 3 === 0) {
        result += lst[i] ** 2;
      }
      if (i % 4 === 0 && i % 3 !== 0) {
        result += lst[i] ** 3;
      }
    }
    return result;
  };

  //*
  Examples:
  for lst = [1,2,3] the output should be 6
  for lst = []  the output should be 0
  for lst = [-1,-5,2,-1,-5]  the output should be -126
  */
  const sumSquares = (lst) => {
    let result = 0;
    for (let i = 0; i < lst.length; i++) {
      if (i % 3 === 0) {
        result += Math.pow(lst[i], 2);
      }
      if (i % 4 === 0 && i % 3 !== 0) {
        result += Math.pow(lst[i], 3);
      }
    }
    return result;
  };

  //*
  Examples:
  for lst = [1,2,3]