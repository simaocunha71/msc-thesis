  let s = {};
  let i = 0;
  while (i < l.length) {
    let k = l[i];
    if (k in s) {
      return true;
    } else {
      s[l[i + 1] - k] = true;
    }
    i += 1;
  }
  return false;
}



