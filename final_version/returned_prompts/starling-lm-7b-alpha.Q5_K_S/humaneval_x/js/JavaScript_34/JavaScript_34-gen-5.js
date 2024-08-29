  let s = [];
  let t = [];
  for (let i = 0; i < l.length; i++) {
    if (s.indexOf(l[i]) === -1) {
      s.push(l[i]);
      t.push(l[i]);
    }
  }
  return t.sort((a, b) => a - b);
}



