  var result = [];
  var max_so_far 

  for  (let num of numbers){
    max_so_far = max_so_far  ? Math.max(max_so_far, num) : num;
    result.push(max_so_far)
  }

  return result;
}



