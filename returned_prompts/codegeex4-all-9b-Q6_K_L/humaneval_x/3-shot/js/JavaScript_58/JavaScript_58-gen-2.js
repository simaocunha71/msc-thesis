  let result = [];
  for (const i of l1) {
    if (l2.includes(i) && !result.includes(i)) {
      result.push(i);
    }
  }
  return result.sort();
}

