  let result = [];
  let index = 0;
  while (index < l.length) {
    if (index % 3 !== 0) {
      result.push(l[index]);
      index += 1;
    } else {
      let number = l[index];
      let sorted = l.slice(0).sort((a, b) => a - b);
      result.push(sorted[index]);
      index += 1;
    }
  }
  return result;
}



