  let pile = [n];
  for (let i = 1; i < n; i++) {
    if (n % 2 == 0) {
      pile.push(pile[i-1] + 2);
    } else {
      pile.push(pile[i-1] + 2);
    }
  }
  return pile;
}



