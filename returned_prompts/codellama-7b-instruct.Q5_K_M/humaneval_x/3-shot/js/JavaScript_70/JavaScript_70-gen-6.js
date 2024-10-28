  lst.sort();
  for (var i = 0; i < lst.length; i++) {
    if (lst[i] == lst[lst.length - 1]) {
      lst.splice(i, 1);
    }
  }
  return lst;
}



