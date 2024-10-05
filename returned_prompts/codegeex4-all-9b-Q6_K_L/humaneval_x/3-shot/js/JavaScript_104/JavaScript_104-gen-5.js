  return x.filter(num => String(num).split("").every(digit => digit % 2 !== 0)).sort((a, b) => a - b);
}



