  return nums.filter(num => Math.abs(num) > 10 && [...`${Math.abs(num)}`].every(digit => [1, 3, 5, 7, 9].includes(parseInt(digit)))).length;
}



