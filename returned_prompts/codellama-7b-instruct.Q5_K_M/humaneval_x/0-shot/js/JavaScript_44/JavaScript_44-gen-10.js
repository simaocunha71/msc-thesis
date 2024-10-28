const changeBase = (x, base) => {
  let rem;
  let str = '';
  while (x > 0) {
    rem = x % base;
    str = rem.toString() + str;
    x = (x - rem) / base;
  }
  return str;
};
