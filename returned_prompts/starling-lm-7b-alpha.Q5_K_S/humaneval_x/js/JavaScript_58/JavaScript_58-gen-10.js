  let result = [...new Set(l1.concat(l2))];
  result = result.filter(el => l1.includes(el) && l2.includes(el));
  result.sort((a, b) => a - b);
  return result;
}



