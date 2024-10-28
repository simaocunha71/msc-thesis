const compare = (a,b) => {
  if (typeof a === 'number' && typeof b === 'number') {
    return a > b ? a : b;
  } else if (typeof a === 'string' && typeof b === 'string') {
    const num1 = parseFloat(a.replace(/[^0-9.,]+/g,""));
    const num2 = parseFloat(b.replace(/[^0-9.,]+/g,""));
    if (isNaN(num1) && isNaN(num2)) {
      return null;
    } else if (isNaN(num1)) {
      return num2;
    } else if (isNaN(num2)) {
      return num1;
    } else if (num1 > num2) {
      return num1;
    } else {
      return num2;
    }
  } else if (typeof a === 'string' && typeof b === 'number') {
    const num1 = parseFloat(a.replace(/[^0-9.,]+/g,""));
    if (isNaN(num1)) {
      return b;
    } else {
      return num1 > b ? num1 : b;
    }
  } else if (typeof a === 'number' && typeof b === 'string') {
    const num2 = parseFloat(b.replace(/[^0-9.,]+/g,""));
    if (isNaN(num2)) {
      return a;
    } else {
      return num2 > a ? num2 : a;
    }
  }
};
return compare(a,b);
};

*/


































































































































