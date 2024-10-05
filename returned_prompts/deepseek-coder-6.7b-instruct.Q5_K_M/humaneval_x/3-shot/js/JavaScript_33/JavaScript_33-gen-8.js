  let sortable = [];
  for (let i = 0; i < l.length; i+=3) {
    sortable.push(l[i]);
  }
  sortable.sort((a, b) => a - b);
  for (let i = 0, j = 0; i < l.length; i+=3) {
    l[i] = sortable[j++];
  }
  return l;
}



