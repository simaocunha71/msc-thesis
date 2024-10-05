  return x.filter(num => !(num.toString().split('').some(n => n % 2 === 0))).sort((a, b) => a - b);
}



