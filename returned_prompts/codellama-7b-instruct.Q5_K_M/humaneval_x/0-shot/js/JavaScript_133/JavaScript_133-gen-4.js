const sumSquares = (lst) => {
    const arr = [];
    for (let i = 0; i < lst.length; i++) {
        arr.push(Math.ceil(lst[i]));
    }
    const sum = arr.reduce((a, b) => a + Math.pow(b, 2), 0);
    return sum;
};

/*
  https://www.codewars.com/kata/54662f7f8f4a7f5a8600009e
*/
