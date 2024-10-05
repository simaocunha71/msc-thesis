  let seen 		= new Set();
  let result = [];

  for  (let num of numbers) {
    if  (!seen.has(num)) {
      result.push(num);
      seen.add(num);
    }
  }

  return result;
}



