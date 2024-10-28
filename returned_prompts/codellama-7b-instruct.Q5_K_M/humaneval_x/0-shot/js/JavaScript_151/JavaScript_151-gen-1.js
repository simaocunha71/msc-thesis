  const doubleTheDifference = (lst) => {
    let sum = 0;
    let oddList = [];
    for (let i = 0; i < lst.length; i++) {
      if (lst[i] % 2 !== 0) {
        oddList.push(lst[i]);
      }
    }
    for (let i = 0; i < oddList.length; i++) {
      sum += Math.pow(oddList[i], 2);
    }
    return sum;
  };

B:
  const doubleTheDifference = (lst) => {
    let sum = 0;
    for (let i = 0; i < lst.length; i++) {
      if (lst[i] % 2 !== 0) {
        sum += Math.pow(lst[i], 2);
      }
    }
    return sum;
  };

C:
  const doubleTheDifference = (lst) => {
    return lst.filter(num => num % 2 !== 0)
      .map(num => Math.pow(num, 2))
      .reduce((a, b) => a + b);
  };

D:
  const doubleTheDifference = (lst) => {
    return lst.filter(num => num % 2 !== 0)
      .map(num => Math.pow(num, 2))
      .reduce((a, b) => a + b, 0);
  };

E:
  const doubleTheDifference = (lst) => {
    return lst.reduce((a, b) => {
      if (b % 2 !== 0) {
        a += Math.pow(b, 2);
      }
      return a;
    }, 0);
  };

F:
  const doubleTheDifference = (lst) => {
    return lst.filter(num => num % 2 !== 0)
      .map(num => Math.pow(num, 2))
      .reduce((a, b) => a + b, 0);
  };

G:
  const doubleTheDifference = (lst) => {