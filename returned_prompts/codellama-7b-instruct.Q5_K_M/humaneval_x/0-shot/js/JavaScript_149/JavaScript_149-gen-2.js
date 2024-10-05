const list_sort = (lst) => {

B:
const list_sort = (lst) => {
  const sortedList = lst.sort((a, b) => {
    if (a.length < b.length) {
      return -1;
    }
    if (a.length > b.length) {
      return 1;
    }
    if (a < b) {
      return -1;
    }
    if (a > b) {
      return 1;
    }
    return 0;
  });

C:
const list_sort = (lst) => {
  const sortedList = lst.sort((a, b) => {
    if (a.length < b.length) {
      return -1;
    }
    if (a.length > b.length) {
      return 1;
    }
    if (a < b) {
      return -1;
    }
    if (a > b) {
      return 1;
    }
    return 0;
  });
  const result = [];
  for (let i = 0; i < sortedList.length; i++) {
    if (sortedList[i].length % 2 !== 0) {
      result.push(sortedList[i]);
    }
  }
  return result;
};
