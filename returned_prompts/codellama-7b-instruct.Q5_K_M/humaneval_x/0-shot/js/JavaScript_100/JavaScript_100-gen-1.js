const makeAPile = (n) => {
  const pile = [n];
  for (let i = 1; i < n; i++) {
    pile.push(pile[i] + 1);
  }
  return pile;
}

