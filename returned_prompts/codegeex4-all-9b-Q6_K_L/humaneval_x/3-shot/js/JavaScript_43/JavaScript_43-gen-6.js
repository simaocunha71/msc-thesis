  let l_set = new Set(l);

  for (let i = 0; i < l.length; i++) {
    if (l_set.has(-l[i])) {
      return true;
    }
  }

  return false;
}

