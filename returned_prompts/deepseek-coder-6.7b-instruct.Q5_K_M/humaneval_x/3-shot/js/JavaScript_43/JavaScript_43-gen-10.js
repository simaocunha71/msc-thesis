  const set_l = new Set(l);

  for (let num of set_l) {
    if (set_l.has(-num)) {
      return true;
    }
  }

  return false;
}



