  let set1 = new Set(l1);
  let set2 = new Set(l2);

  let common = new Set();
  for (let x of set1) {
    if (set2.has(x)) {
      common.add(x);
    }
  }

  return Array.from(common);
}



