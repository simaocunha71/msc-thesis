  const n = lst.length;
  if (n === 0) {
    return null;
  }
  if (n === 1) {
    return null;
  }

  const sorted_lst = lst.sort();

  for (let i = 0; i < n; i++) {
    if (lst[i] === sorted_lst[i + 1]) {
      return sorted_lst[i + 1];
    }
  }
}



