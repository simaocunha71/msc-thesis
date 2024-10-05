  let result = [];
  let counter = 0;

  while (lst.length > 0) {
    if (counter % 2 == 0) {
      let min = Math.min(...lst);
      result.push(min);
      lst.splice(lst.indexOf(min), 1);
    } else {
      let max = Math.max(...lst);
      result.push(max);
      lst.splice(lst.indexOf(max), 1);
    }
    counter += 1;
  }

  return result;
}



