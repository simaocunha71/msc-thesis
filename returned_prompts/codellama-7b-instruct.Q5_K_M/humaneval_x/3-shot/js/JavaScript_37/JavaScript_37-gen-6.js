  const sorted_list = [];

  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      sorted_list.push(l[i]);
    } else {
      sorted_list.push(l[i].sort());
    }
  }

  return sorted_list;
}



