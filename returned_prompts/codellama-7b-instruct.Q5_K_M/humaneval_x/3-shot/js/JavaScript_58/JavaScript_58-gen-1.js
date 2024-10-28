  var result = [];
  var l1_set = new Set(l1);
  var l2_set = new Set(l2);
  for (let i = 0; i < l1.length; i++) {
    if (l2_set.has(l1[i])) {
      result.push(l1[i]);
    }
  }
  return result;
}



