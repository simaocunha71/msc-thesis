  lst = lst.filter(word => word.length % 2 === 0);
  lst.sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    } else {
      return a.length - b.length;
    }
  });
  return lst;
}
// If you want to return the sum of the strings, you can use reduce method
// const sortedListSum = (lst) => lst.filter(word => word.length % 2 === 0).sort((a, b) => a.length - b.length).reduce((acc, current) => acc + current, '');
// This will return the sum of the strings in the list, but it will not preserve the order of the strings.



