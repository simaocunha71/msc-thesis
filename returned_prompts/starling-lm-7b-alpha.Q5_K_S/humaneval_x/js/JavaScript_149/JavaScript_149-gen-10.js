  lst = lst.filter(String.prototype.length % 2 === 0);
  lst.sort((a, b) => {
    if (a.length < b.length) return -1;
    if (a.length > b.length) return 1;
    return a.localeCompare(b);
  });
  return lst;
}



