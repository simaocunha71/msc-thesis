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
  let min;
  const max = lst.reduce(((accumulator, currentValue) => {
    accumulator += Math.max(...(currentValue)) + 1; // adding 1 to the max
    return accumulator;
  }, 0);

  for (let i = min = 0; min <= max; min++) {
    lst[min] = lst[min];
  }
  while (i < lst.length) {
    if (lst[i] > lst[(max - 1)] || i === lst.length) {
      return lst;
    } else {
      lst[max] = lst[max];
    }
    max--;
  }
};
