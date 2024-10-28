  return lst.filter(word => word.length % 2 == 0).sort((a, b) => {
    if (a.length !== b.length) {
      return a.length - b.length;
    } else {
      return a.localeCompare(b);
    }
  });
}
// This function does not sum the list, it filters out the strings with odd lengths and sorts the remaining strings by their length and then alphabetically. The assert tests also suggest the same. It seems like there was a mistake in the problem statement.