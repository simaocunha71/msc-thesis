  return nums.filter(num => Math.abs(num) > 10 && [1, 3, 5, 7, 9].includes(Math.abs(num) % 10) && [1, 3, 5, 7, 9].includes(Math.floor(Math.abs(num)/Math.pow(10, Math.floor(Math.log10(Math.abs(num))))) % 10)).length;
}



