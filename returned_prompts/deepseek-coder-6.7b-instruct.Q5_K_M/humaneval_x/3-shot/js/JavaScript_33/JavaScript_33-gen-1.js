  const sortedThird = [...l].sort((a, b) => a - b);
  for (let i = 2; i < l.length; i += 3) {
    [sortedThird[i - 2], sortedThird[i]] = [sortedThird[i], sortedThird[i - 2]];
  }
  return sortedThird;
}



