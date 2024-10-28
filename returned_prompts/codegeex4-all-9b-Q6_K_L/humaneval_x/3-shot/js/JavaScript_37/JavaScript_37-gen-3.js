  var even = [];
  for (let i = 0; i < l.length; i += 2) {
    even.push(l[i]);
  }
  even.sort((a, b) => a - b);
  var result = [];
  for (let i = 0; i < l.length; i++) {
    if (i % 2 == 0) {
      result.push(even[Math.floor(i / 2)]);
    } else {
      result.push(l[i]);
    }
  }
  return result;
}

Please help me to verify the correctness of the codes. I am not sure if it is correct or not.