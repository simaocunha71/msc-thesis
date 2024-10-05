const circularShift = (x, shift) => {
  x = x.toString();
  let result = '';
  let newShift = shift;
  if (shift > x.length) {
    newShift = x.length;
  }
  for (let i = newShift; i < x.length; i++) {
    result += x[i];
  }
  for (let i = 0; i < newShift; i++) {
    result += x[i];
  }
  return result;
};

