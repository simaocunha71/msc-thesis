/*
  First, we generate the array a as described in the problem statement.
  Then, we iterate through the array a three times to find all triples (a[i], a[j], a[k]).
  If the sum of the triple is a multiple of 3, we increment a counter.
  Finally, we return the counter.
  */
const getMaxTriples = (n) => {
  let a = [];
  for (let i = 1; i <= n; i++) {
    a.push(i * i - i + 1);
  }

  let counter = 0;
  for (let i = 0; i < n - 2; i++) {
    for (let j = i + 1; j < n - 1; j++) {
      for (let k = j + 1; k < n; k++) {
        if ((a[i] + a[j] + a[k]) % 3 === 0) {
          counter++;
        }
      }
    }
  }
  return counter;
}