  if (lst.length === 0) {
    return lst;
  }

  let sorted = lst.slice().sort((a, b) => a - b);
  let result = [];
  let i = 0, j = sorted.length - 1;

  while (i <= j) {
    result.push(sorted[i]);
    i++;
    if (i <= j) {
      result.push(sorted[j]);
      j--;
    }
  }

  return result;
}
// OR
const strangeSortList = (lst) => {
  if (lst.length === 0) {
    return lst;
  }

  let sorted = lst.slice().sort((a, b) => a - b);
  let result = [];
  let min = 0, max = sorted.length - 1;

  while (min <= max) {
    result.push(sorted[min]);
    min++;
    if (min <= max) {
      result.push(sorted[max]);
      max--;
    }
  }

  return result;
}