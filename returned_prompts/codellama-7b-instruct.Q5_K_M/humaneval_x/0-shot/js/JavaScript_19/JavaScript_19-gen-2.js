const sortNumbers = (numbers) => {
  const arr = numbers.split(' ');
  return arr.sort((a, b) => a - b).join(' ');
};
