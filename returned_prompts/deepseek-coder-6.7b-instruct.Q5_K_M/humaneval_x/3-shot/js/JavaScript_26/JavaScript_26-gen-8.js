  var result = [];
  var seen = {};

  for  (const n of numbers) {
    if  (!seen[n]) {
      result.push(n);
      seen[n] = true;
     }
  }

  return result;
}



