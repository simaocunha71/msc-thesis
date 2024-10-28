const filterByPrefix = (strings, prefix) => {
  let arr = [];
  for (let i = 0; i < strings.length; i++) {
    if (strings[i].startsWith(prefix)) {
      arr.push(strings[i]);
    }
  }
  return arr;
};
