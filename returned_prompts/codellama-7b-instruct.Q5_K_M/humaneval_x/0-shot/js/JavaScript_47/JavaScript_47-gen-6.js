  /*Return median of elements in the list l.
  >>> median([3, 1, 2, 4, 5])
  3
  >>> median([-10, 4, 6, 1000, 10, 20])
  8.0
  */
const median = (l) => {
    l.sort();
    const mid = Math.floor(l.length / 2);
    return l.length % 2 ? l[mid] : (l[mid - 1] + l[mid]) / 2;
};
