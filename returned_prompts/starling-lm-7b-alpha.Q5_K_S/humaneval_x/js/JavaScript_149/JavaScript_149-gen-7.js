  let result = [];
  let temp = lst.filter(s => s.length % 2 === 0);
  temp.sort((a, b) => a.length - b.length || a.localeCompare(b));
  result = result.concat(temp);
  temp = lst.filter(s => s.length % 2 === 1);
  temp.sort((a, b) => a.length - b.length || a.localeCompare(b));
  result = result.concat(temp);
  return result;
}



