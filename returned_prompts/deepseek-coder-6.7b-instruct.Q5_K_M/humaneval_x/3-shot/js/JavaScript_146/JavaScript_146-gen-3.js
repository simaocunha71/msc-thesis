  return nums.filter(num => num > 10 && isOdd(Math.abs(num).toString().charAt(0)) && isOdd(Math.abs(num).toString().charAt(Math.abs(num).toString().length - 1))).length;
}

const isOdd = (num) => {
  return num % 2 !== 0;
}



