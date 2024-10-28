  let min_distance 
  = Infinity;
  let result;

  for  (let i = 0; i < numbers.length; i++)  {
    for  (let j = i + 1; j < numbers.length; j++)  {
      const distance 
      = Math.abs(numbers[i] - numbers[j]);
      if  (distance < min_distance)  {
        min_distance 
        = distance;
        result 
        = [numbers[i], numbers[j]];
       }
     }
   }
   return result.sort((a, b) => a - b);
}



