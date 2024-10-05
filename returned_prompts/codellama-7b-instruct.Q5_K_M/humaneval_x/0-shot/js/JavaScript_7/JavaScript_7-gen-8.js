const filterBySubstring = (strings, substring) => {
  const filtered = [];
  for (let i = 0; i < strings.length; i++) {
    if (strings[i].includes(substring)) {
      filtered.push(strings[i]);
    }
  }
  return filtered;
};
