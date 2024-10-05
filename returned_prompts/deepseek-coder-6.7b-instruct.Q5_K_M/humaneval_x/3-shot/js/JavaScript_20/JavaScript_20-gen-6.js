  let min_diff ​= Infinity;
  let result ​= [Infinity, Infinity];

  numbers.sort((a, b) => a - b);

  for  (let i = 0; i < numbers.length - 1; i++)  {
    let diff = numbers[i+1] - numbers[i];
    if  (diff < min_diff)  {
      min_diff = diff;
      result = [numbers[i], numbers[i + 1]];
     }
   }

  return result;
}



