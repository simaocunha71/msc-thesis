const prodSigns = (arr) => {
  let result = 0;
  if (arr.length === 0) return null;
  for (let i = 0; i < arr.length; i++) {
    result += Math.abs(arr[i]) * (arr[i] > 0 ? 1 : -1);
  }
  return result;
};


// 
