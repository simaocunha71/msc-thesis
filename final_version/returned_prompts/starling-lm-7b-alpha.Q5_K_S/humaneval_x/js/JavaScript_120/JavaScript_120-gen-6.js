  const result = [];
  for (let i = 0; i < k; i++) {
    result.push(Math.max(...arr));
    arr.splice(arr.indexOf(Math.max(...arr)), 1);
  }
  return result;
};



