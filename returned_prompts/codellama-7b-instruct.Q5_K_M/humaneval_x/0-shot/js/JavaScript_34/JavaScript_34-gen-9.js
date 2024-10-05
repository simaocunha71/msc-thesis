const unique = (l) => {
  let newList = [];
  for (const i of l) {
    if (!newList.includes(i)) {
      newList.push(i);
    }
  }
  return newList.sort((a, b) => a - b);
};
