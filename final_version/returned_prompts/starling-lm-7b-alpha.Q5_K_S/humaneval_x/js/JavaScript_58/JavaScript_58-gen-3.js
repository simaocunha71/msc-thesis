  let result = [];
  let set1 = new Set(l1);
  for (let i = 0; i < l2.length; i++) {
    if (set1.has(l2[i])) {
      result.push(l2[i]);
      set1.delete(l2[i]);
    }
  }
  return result;
}



