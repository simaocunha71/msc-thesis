/*
  Given list of integers, return list in strange order.
  Strange sorting, is when you start with the minimum value,
  then maximum of the remaining integers, then minimum and so on.

  Examples:
  strangeSortList([1, 2, 3, 4]) == [1, 4, 2, 3]
  strangeSortList([5, 5, 5, 5]) == [5, 5, 5, 5]
  strangeSortList([]) == []
  */
const strangeSortList = (lst) => {
  if (lst.length === 0) return [];
  let sortedList = lst.slice().sort((a, b) => a - b);
  let result = [];
  let minIndex = 0;
  let maxIndex = lst.length - 1;
  let isMin = true;
  while (minIndex <= maxIndex) {
    if (isMin) {
      result.push(sortedList[minIndex]);
      minIndex++;
    } else {
      result.push(sortedList[maxIndex]);
      maxIndex--;
    }
    isMin = !isMin;
  }
  return result;
};