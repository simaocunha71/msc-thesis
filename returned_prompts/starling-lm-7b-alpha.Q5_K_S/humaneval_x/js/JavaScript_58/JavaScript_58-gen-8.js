  let unique = [...new Set(l1.concat(l2))];
  unique.sort((a, b) => a - b);
  let result = [];
  for (const item of unique) {
    if (l1.includes(item) && l2.includes(item)) {
      result.push(item);
    }
  }
  return result;
}



