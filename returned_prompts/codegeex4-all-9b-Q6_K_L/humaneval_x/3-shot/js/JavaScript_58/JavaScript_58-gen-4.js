  var common = [];

  for (const x of l1) {
    if (l2.includes(x) && !common.includes(x)) {
      common.push(x);
    }
  }

  common.sort((a, b) => a - b);
  return common;
}