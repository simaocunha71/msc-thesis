  return x.filter(n => !/\d+/.exec(n.toString()).some(digit => parseInt(digit) % 2 === 0)).sort((a, b) => a - b);
}