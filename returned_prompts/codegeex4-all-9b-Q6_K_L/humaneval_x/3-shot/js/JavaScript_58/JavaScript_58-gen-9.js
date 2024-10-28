  var result = [];
  var set_l1 = new Set(l1);
  var set_l2 = new Set(l2);

  for (const i of set_l1) {
    if (set_l2.has(i)) {
      result.push(i);
    }
  }

  return result.sort();
}



