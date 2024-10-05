const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const binA = a.toString(2);
    const binB = b.toString(2);
    const onesA = binA.split('1').length - 1;
    const onesB = binB.split('1').length - 1;
    if (onesA !== onesB) {
      return onesA - onesB;
    }
    return a - b;
  });
};

B:
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const binA = a.toString(2);
    const binB = b.toString(2);
    return binA.split('1').length - 1 - binB.split('1').length + 1 || a - b;
  });
};
