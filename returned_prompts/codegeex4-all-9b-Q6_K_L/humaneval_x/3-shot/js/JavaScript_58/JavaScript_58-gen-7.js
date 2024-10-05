  let result = [];
  for (const e of l1) {
    if (l2.includes(e) && !result.includes(e)) {
      result.push(e);
    }
  }
  result.sort();
  return result;
}



