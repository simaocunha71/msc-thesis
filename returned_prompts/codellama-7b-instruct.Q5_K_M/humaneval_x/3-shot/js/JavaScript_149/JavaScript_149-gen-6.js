  const odds = lst.filter((w) => w.length % 2 == 1);
  const evens = lst.filter((w) => w.length % 2 == 0);
  const sortedOdds = odds.sort((a, b) => a.length - b.length);
  const sortedEvens = evens.sort((a, b) => a.length - b.length);
  const sorted = sortedOdds.concat(sortedEvens);
  return sorted;
}



