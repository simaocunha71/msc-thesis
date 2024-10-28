  let set = new Set();
  for (let i = 0; i < l.length; i++) {
    if (set.has(-l[i])) {
      return true;
    } else {
      set.add(l[i]);
    }
  }
  return false;
}



