  let set = new Set(l);
  for (let i = 0; i < l.length; i++) {
    for (let j = i + 1; j < l.length; j++) {
      let target = l[i] + l[j];
      if (set.has(-target)) {
        return true;
      }
    }
  }
  return false;
}



