const list_sort = (arr) => {
  return arr.filter((word) => word.length % 2 === 0).sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
};

console.log(list_sort(["aa", "a", "aaa"])); // ["aa"]
console.log(list_sort(["ab", "a", "aaa", "cd"])); // ["ab", "cd"]

