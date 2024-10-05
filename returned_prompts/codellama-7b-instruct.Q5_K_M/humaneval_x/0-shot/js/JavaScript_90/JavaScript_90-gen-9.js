const nextSmallest = (lst) => {
  let small = null;
  for (const i of lst) {
    if (small === null || small > i) small = i;
  }
  return small;
}
