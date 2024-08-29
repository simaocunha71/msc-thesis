  let result = [0, 0];
  let max = Math.floor(n / 2);
  for (let i = 1; i <= max; i++) {
    let num = i.toString();
    if (num.length % 2 === 0) {
      result[0]++;
    } else {
      result[1]++;
    }
    if (num === num.split('').reverse().join('')) {
      result[num % 2]++;
    }
  }
  return result;
}



