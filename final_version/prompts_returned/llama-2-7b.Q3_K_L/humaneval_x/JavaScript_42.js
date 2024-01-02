/*Return list with elements incremented by 1.
  >>> incrList([1, 2, 3])
  [2, 3, 4]
  >>> incrList([5, 3, 5, 2, 3, 3, 9, 0, 123])
  [6, 4, 6, 3, 4, 4, 10, 1, 124]
  */
const incrList = (l) => {
  let n = l.length;
  for (let i=0 ; i<n ; i++) {
    // console.log(l[i]);
    if (!isNaN(parseInt(l[i]))) {
      l[i]=parseInt(l[i])+1;
    } else {
      l[i]="!" + l[i];
    }
  }
  return [...l];
}