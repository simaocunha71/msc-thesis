  let result = [];
  let even = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 === 0) {
      result.push(l[i]);
    } else {
      even.push(l[i]);
    }
  }
  even.sort();
  for (let i = 0; i < even.length; i++) {
    result.push(even[i]);
  }
  return result;
}



