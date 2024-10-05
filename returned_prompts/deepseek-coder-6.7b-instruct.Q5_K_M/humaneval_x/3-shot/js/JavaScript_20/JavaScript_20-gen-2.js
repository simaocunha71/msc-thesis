  let min_difference = Infinity;
  let closest_elements = (null, null);

  for  (let i = 0; i < numbers.length; i++)  {
    for  (let j = i + 1; j < numbers.length; j++)  {
      let difference = Math.abs(numbers[i] - numbers[j]);
      if  (difference < min_difference)  {
        min_difference = difference;
        closest_elements = (numbers[i], numbers[j]);
      }
    }
  }

  return closest_elements.sort()[0], closest_elements.sort()[1];
}



