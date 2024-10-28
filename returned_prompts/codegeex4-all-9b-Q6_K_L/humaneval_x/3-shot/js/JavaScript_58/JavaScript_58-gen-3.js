  let result = [];
  for (let i = 0; i < l1.length; i++) {
    for (let j = 0; j < l2.length; j++) {
      if (l1[i] == l2[j]) {
        result.push(l1[i]);
        break;
      }
    }
  }
  return [...new Set(result)];
}



