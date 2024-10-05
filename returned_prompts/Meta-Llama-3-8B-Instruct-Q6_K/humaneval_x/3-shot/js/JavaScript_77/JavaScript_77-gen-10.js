  let c = 0;
  while (Math.pow(c, 3) <= a) {
    if (Math.pow(c, 3) === a) {
      return true;
    }
    c++;
  }
  return false;
}
//or
const iscube = (a) => {
  let c = Math.ceil(Math.cbrt(a));
  return Math.pow(c, 3) === a;
}
//or
const iscube = (a) => {
  let c = Math.floor(Math.cbrt(a));
  return Math.pow(c, 3) === a;
}
//or
const iscube = (a) => {
  let c = Math.floor(Math.cbrt(a));
  return c * c * c === a;
}