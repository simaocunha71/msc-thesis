  let result = [numbers[0]];
  for (let i = 1; i < numbers.length; i++) {
    result.push(Math.max(result[i-1], numbers[i]));
  }
  return result;
}
// OR
const rollingMax = (numbers) => {
  let max = numbers[0];
  let result = [max];
  for (let i = 1; i < numbers.length; i++) {
    max = Math.max(max, numbers[i]);
    result.push(max);
  }
  return result;
}