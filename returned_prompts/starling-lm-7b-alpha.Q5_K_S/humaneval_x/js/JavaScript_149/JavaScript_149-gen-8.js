  let new_lst = lst.filter(word => word.length % 2 === 0);
  new_lst.sort((a, b) => {
    if (a.length === b.length) {
      return a.localeCompare(b);
    }
    return a.length - b.length;
  });
  return new_lst;
}



