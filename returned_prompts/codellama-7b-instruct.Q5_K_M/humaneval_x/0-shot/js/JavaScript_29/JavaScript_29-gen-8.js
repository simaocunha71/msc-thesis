const filterByPrefix = (strings, prefix) => strings.filter(str => str.startsWith(prefix));

B:
const filterByPrefix = (strings, prefix) => {
  const result = [];
  for (let i = 0; i < strings.length; i++) {
    if (strings[i].startsWith(prefix)) {
      result.push(strings[i]);
    }
  }
  return result;
};

C:
const filterByPrefix = (strings, prefix) => {
  return strings.filter((str, i) => str.startsWith(prefix));
};
