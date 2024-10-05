  let str = a;
  let n = b.length;
  for (let i = 0; i < n; i++) {
    if (str.includes(b)) {
      return true;
    }
    str = str.slice(1) + str[0];
  }
  return false;
}