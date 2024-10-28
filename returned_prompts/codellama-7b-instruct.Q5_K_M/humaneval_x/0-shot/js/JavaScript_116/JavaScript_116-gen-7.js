const sortArray = (arr) => {
  let sorted = [];
  let binary = [];
  let decimal = [];

  for (let i = 0; i < arr.length; i++) {
    binary.push(arr[i].toString(2));
    decimal.push(arr[i]);
  }
  binary.sort((a, b) => a.length - b.length || a.localeCompare(b));
  for (let i = 0; i < binary.length; i++) {
    for (let j = 0; j < arr.length; j++) {
      if (binary[i] === decimal[j].toString(2)) {
        sorted.push(decimal[j]);
      }
    }
  }
  return sorted;
};

B:
const sortArray = (arr) => {
  return arr.sort((a, b) => a.toString(2).length - b.toString(2).length || a - b);
};

C:
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const aBinary = a.toString(2);
    const bBinary = b.toString(2);
    return aBinary.length - bBinary.length || aBinary.localeCompare(bBinary);
  });
};

D:
const sortArray = (arr) => {
  return arr.sort((a, b) => a.toString(2).length - b.toString(2).length || a - b);
};

E:
const sortArray = (arr) => {
  return arr.sort((a, b) => {
    const aBinary = a.toString(2);
    const bBinary = b.toString(2);
    return aBinary.length - bBinary.length || aBinary.localeCompare(bBinary);
  });
};

F:
const sortArray = (arr) => {
  return arr.sort((a, b) => a.toString(2).length - b.toString(2).length || a - b);
};

G:
const sortArray = (arr) => {
  return arr.sort((a, b) =>