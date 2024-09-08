  let s = new Set(l);
  for (let i = 0; i < l.length; i++) {
    let target = -l[i];
    if (s.has(target)) {
      return true;
    }
  }
  return false;
}



