  const len = l.length;
  let res = false;
  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      for (let k = j + 1; k < len; k++) {
        if (l[i] + l[j] + l[k] === 0) {
          res = true;
          break;
        }
      }
    }
  }
  return res;
}



