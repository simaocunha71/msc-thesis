const cycpatternCheck = (a, b) => {
  a = a.toLowerCase();
  b = b.toLowerCase();
  let arr = [...b];
  let str = "";
  for (let i = 0; i < arr.length; i++) {
    str += arr.shift();
  }
  arr = [...str];
  for (let i = 0; i < arr.length; i++) {
    if (a.includes(arr[i])) {
      return true;
    }
  }
  return false;
};

