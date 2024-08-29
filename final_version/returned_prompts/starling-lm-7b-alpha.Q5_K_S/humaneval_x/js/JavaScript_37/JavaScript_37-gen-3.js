  let result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 === 0) {
      result.push(l[i]);
    } else {
      result.push(l[i]);
    }
  }
  result = result.slice(0, result.length / 2);
  result = result.concat(result.slice(result.length / 2));
  return result;
}



