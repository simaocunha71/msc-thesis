  let result = [];
  let length = Math.min(l1.length, l2.length);
  for (let i = 0; i < length; i++) {
    if (l1[i] === l2[i] && result.indexOf(l1[i]) === -1) {
      result.push(l1[i]);
    }
  }
  return result;
}



