  return nums.filter(n => Math.abs(n) > 10 && [...(Math.abs(n)+'')].every(d => [1, 3, 5, 7, 9].includes(parseInt(d)))).length;
}



