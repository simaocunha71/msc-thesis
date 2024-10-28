  const sorted_l = l.sort((a, b) => a - b);
  for (let i = 1; i < l.length; i++) {
    if (sorted_l[i] < sorted_l[i - 1]) {
      return false;
    }
  }
  return true;
}



