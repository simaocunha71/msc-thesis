  let max = -1;
  for (let i of lst) {
    if (i > 0 && lst.filter(x => x === i).length >= i) {
      max = i;
    }
  }
  return max;
}
// OR
const search = (lst) => {
  let max = -1;
  for (let i of lst) {
    if (i > 0 && lst.filter(x => x === i).length >= i) {
      if (i > max) {
        max = i;
      }
    }
  }
  return max;
} // This one also returns -1 if no such value exists.