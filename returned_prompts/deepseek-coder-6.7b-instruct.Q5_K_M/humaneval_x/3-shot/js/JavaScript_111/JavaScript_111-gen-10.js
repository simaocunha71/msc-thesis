  let count = {};
  test.split(' ').forEach(function(s) {
    count[s] = (count[s] || 0) + 1;
  });

  let maxCount = Math.max(...Object.values(count));
  let result = {};

  for(let key in count) {
    if(count[key] === maxCount) {
      result[key] = count[key];
    }
  }

  return result;
}



