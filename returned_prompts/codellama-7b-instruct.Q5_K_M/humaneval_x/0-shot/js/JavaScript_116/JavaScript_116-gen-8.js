const sortArray = (arr) => {
  return arr.sort((a, b) => {
    if (a.toString(2).split('1').length === b.toString(2).split('1').length) {
      return a - b;
    }
    return a.toString(2).split('1').length - b.toString(2).split('1').length;
  });
};

const sortArray = (arr) => {
  return arr.sort((a, b) => {
    if (a.toString(2).split('1').length === b.toString(2).split('1').length) {
      return a - b;
    }
    return a.toString(2).split('1').length - b.toString(2).split('1').length;
  });
};

const sortArray = (arr) => {
  return arr.sort((a, b) => {
    let aBin = a.toString(2);
    let bBin = b.toString(2);
    if (aBin.match(/1/g).length === bBin.match(/1/g).length) {
      return a - b;
    }
    return aBin.match(/1/g).length - bBin.match(/1/g).length;
  });
};

const sortArray = (arr) => {
  return arr.sort((a, b) => {
    let aBin = a.toString(2);
    let bBin = b.toString(2);
    if (aBin.split('1').length === bBin.split('1').length) {
      return a - b;
    }
    return aBin.split('1').length - bBin.split('1').length;
  });
};

const sortArray = (arr) => {
  return arr.sort((a, b) => {
    let aBin = a.toString(2);
    let bBin = b.toString(2);
    if (aBin.match(/1/g).length === bBin.match(/1/g).length) {
      return a - b;
    }
