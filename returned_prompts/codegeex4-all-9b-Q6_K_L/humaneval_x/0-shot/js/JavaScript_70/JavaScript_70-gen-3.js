const strangeSortList = (lst) => {
  let result = [];
  let minMax = true;
  let min = 0;
  let max = lst.length - 1;
  while (min <= max) {
    if (minMax) {
      result.push(lst[min]);
      min++;
    } else {
      result.push(lst[max]);
      max--;
    }
    minMax = !minMax;
  }
  return result;
}