const sortArray = (arr) => {
  arr.sort((a, b) => {
    const aOnes = a.toString(2).match(/1/g).length;
    const bOnes = b.toString(2).match(/1/g).length;
    if (aOnes === bOnes) {
      return a - b;
    }
    return aOnes - bOnes;
  });
  return arr;
};

B:
const sortArray = (arr) => {
  arr.sort((a, b) => {
    const aOnes = a.toString(2).split('').filter(x => x === '1').length;
    const bOnes = b.toString(2).split('').filter(x => x === '1').length;
    if (aOnes === bOnes) {
      return a - b;
    }
    return aOnes - bOnes;
  });
  return arr;
};

C:
const sortArray = (arr) => {
  arr.sort((a, b) => {
    const aOnes = a.toString(2).match(/1/g).length;
    const bOnes = b.toString(2).match(/1/g).length;
    if (aOnes === bOnes) {
      return a - b;
    }
    return aOnes - bOnes;
  });
  return arr;
};

D:
const sortArray = (arr) => {
  arr.sort((a, b) => {
    const aOnes = a.toString(2).split('').filter(x => x === '1').length;
    const bOnes = b.toString(2).split('').filter(x => x === '1').length;
    if (aOnes === bOnes) {
      return a - b;
    }
    return aOnes - bOnes;
  });
  return arr;
};
