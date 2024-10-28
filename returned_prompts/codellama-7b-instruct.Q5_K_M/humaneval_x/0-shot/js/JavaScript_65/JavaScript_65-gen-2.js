const circularShift = (x, shift) => {
  let str = x.toString();
  let len = str.length;
  let res = '';
  for (let i = 0; i < len; i++) {
    let index = (i + shift) % len;
    res += str[index];
  }
  return res;
}
