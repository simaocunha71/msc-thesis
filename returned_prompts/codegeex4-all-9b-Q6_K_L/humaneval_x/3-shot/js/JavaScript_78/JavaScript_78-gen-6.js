  const hexToDec = hex => parseInt(hex, 16);
  const isPrime = num => {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };
  return num.split('').filter(x => [2, 3, 5, 7, 11, 13].includes(hexToDec(x))).length;
}

// or
const hexKey = (num) => {
  const hexToDec = hex => parseInt(hex, 16);
  const isPrime = num => {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };
  return num.split('').filter(x => '237'.includes(x) || 'ABD'.includes(x.toUpperCase())).length;
}