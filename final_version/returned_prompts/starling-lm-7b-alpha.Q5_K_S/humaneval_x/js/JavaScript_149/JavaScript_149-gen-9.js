  lst = lst.filter(word => word.length % 2 == 0);
  lst.sort((a, b) => (a.length == b.length) ? a.localeCompare(b) : a.length - b.length);
  return lst;
}



