  let sorted = lst.slice();
  while (sorted.length > 0) {
    let min = Math.min(...sorted);
    sorted.splice(sorted.indexOf(min), 1);
    let max = Math.max(...sorted);
    sorted.splice(sorted.indexOf(max), 1);
  }
  return lst;
}



