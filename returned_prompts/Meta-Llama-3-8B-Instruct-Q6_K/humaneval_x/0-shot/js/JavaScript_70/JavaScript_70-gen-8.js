```
const strangeSortList = (lst) => {
  if (!lst.length) return [];
  const sortedList = lst.slice().sort((a, b) => a - b);
  const result = [];
  let minIndex = 0;
  let maxIndex = lst.length - 1;
  while (maxIndex >= minIndex) {
    result.push(sortedList[minIndex]);
    if (maxIndex > minIndex) {
      result.push(sortedList[maxIndex]);
    }
    minIndex++;
    maxIndex--;
  }
  return result;
};
``` 