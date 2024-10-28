  let newList = lst.filter(word => word.length % 2 === 0);
  newList.sort((a, b) => a.length - b.length || a.localeCompare(b));
  return newList;
}



