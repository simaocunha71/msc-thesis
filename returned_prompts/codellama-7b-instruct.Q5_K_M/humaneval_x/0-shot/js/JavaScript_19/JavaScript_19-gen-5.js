const sortNumbers = numbers => numbers
  .split(' ')
  .sort((a, b) => +a - +b)
  .join(' ');
