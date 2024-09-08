  let sortedList = [];

  while (lst.length > 0) {
    let min = Math.min(...lst);
    sortedList.push(min);
    lst = lst.filter(x => x != min);
  }

  return sortedList;
}



