const startsOneEnds = (n) => {
  let count = 0;
  for (let i = 1; i < 10**n; i++) {
    if (i.toString().startsWith('1')) count++;
    if (i.toString().endsWith('1')) count++;
  }
  return count;
}