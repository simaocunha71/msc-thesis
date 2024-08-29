  const checkIfOdd = (n) => {
    const str_n = String(n);
    for (const d of str_n) {
      if (Number(d) % 2 == 0) {
        return false;
      }
    }
    return true;
  };

  const checkIfUnique = (n) => {
    const str_n = String(n);
    for (const d of str_n) {
      if (str_n.indexOf(d) > 1) {
        return false;
      }
    }
    return true;
  };

  return x
    .filter(checkIfOdd)
    .filter(checkIfUnique)
    .sort((a, b) => a - b);
}



