  const indexes = lst.reduce((acc, curr, index) => {
    if (curr.includes(x)) {
      acc.push(index);
    }
    return acc;
  }, []);

  const indexesSorted = indexes.sort((a, b) => a - b);

  const result = indexesSorted.map((i) => {
    return lst[i].reduceRight((acc, curr, index) => {
      if (curr === x) {
        acc.push(index);
      }
      return acc;
    }, []);
  });

  return result.sort((a, b) => a[0] - b[0]);
};

*/

getRow([
  [1,2,3,4,5,6],
  [1,2,3,4,1,6],
  [1,2,3,4,5,1]
], 1)

// [(0, 0), (1, 4), (1, 0), (2, 5), (2, 0)]

getRow([], 1)

// []

getRow([[], [1], [1, 2, 3]], 3)

// [(2, 2)]

















































































































































































































