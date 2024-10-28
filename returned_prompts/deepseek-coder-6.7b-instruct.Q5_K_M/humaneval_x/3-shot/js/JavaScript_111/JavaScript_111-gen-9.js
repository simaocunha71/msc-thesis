  let count = {};
  let arr = test.split(' ');
  for (let i = 0; i < arr.length; i++){
    if (count[arr[i]]){
      count[arr[i]]++;
    } else {
      count[arr[i]] = 1;
    }
  }
  let maxCount = Math.max(...Object.values(count));
  let result = {};
  for (let key in count){
    if (count[key] === maxCount){
      result[key] = count[key];
    }
  }
  return result;
}



