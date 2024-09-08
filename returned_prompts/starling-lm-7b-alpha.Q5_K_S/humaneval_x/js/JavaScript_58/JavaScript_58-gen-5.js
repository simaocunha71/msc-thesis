  let set = new Set(l2);
  let result = [];
  for (const i of l1) {
    if (set.has(i)) {
      set.delete(i);
      result.push(i);
    }
  }
  return result.sort();
}



