  const deleteOddLengths = (lst) => {
    return lst.filter(word => word.length % 2 === 0);
  };

  const sortByLength = (lst) => {
    return lst.sort((a, b) => a.length - b.length);
  };

  const sortAlphabetically = (lst) => {
    return lst.sort();
  };

  const lst = deleteOddLengths(lst);
  return sortByLength(sortAlphabetically(lst));
};



