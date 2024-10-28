  const oneToNine = [...Array(9).keys()].map(String);
  const filtered = arr.filter(x => x >= 1 && x <= 9);
  const sorted = filtered.sort((a, b) => a - b).reverse();
  return sorted.map(x => oneToNine[+x - 1]);
}