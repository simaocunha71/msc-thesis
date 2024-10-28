  let result = [];
  let row = 0;
  for (let i of lst) {
    let index = i.indexOf(x);
    if (index != -1) {
      result.push([row, index]);
    }
    row += 1;
  }
  return result;
}



