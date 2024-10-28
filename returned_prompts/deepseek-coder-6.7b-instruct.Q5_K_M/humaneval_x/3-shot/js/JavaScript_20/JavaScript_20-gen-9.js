  let min_diff = Infinity;
  let min_pair = null;

  for  (let i = 0; i < numbers.length; i++)  {
    for  (let j = i + 1; j < numbers.length; j++)  {
      let diff = Math.abs(numbers[i] - numbers[j]);
      if  (diff < min_diff)  {
        min_diff = diff;
        min_pair = [numbers[i], numbers[j]];
      }
    }
  }

  return min_pair.sort((a, b) => a - b);
}



