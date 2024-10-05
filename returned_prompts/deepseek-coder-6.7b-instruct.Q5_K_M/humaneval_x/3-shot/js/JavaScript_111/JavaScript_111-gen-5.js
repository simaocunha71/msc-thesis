  let counts = {};
  test.split(' ').forEach(function(s) {
    counts[s] = (counts[s] || 0) + 1;
  });
  let max = Math.max(...Object.values(counts));
  let result = {};
  for(let key in counts){
    if(counts[key] === max){
      result[key] = counts[key];
    }
  }
  return result;
}



