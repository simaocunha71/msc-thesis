  let sortedThird = [...l];
  sortedThird.sort((a, b) => a - b);
  for (let i = 2; i < l.length; i += 3) {
    const temp = sortedThird[i];
    sortedThird[i] = l[i];
    l[i] = temp;
  }
  return l;
}



