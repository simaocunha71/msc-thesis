/*Return median of elements in the list l.
  >>> median([3, 1, 2, 4, 5])
  3
  >>> median([-10, 4, 6, 1000, 10, 20])
  8.0
  */
const median = (l) => {
  if (l.length === 0) {
    throw new Error('List is empty');
  }
  l.sort();
  if (l.length % 2 === 0) {
    return (l[l.length / 2 - 1] + l[l.length / 2]) / 2;
  } else {
    return l[Math.floor(l.length / 2)];
  }
};

