  return x.filter(n => n.toString().split('').every(digit => digit % 2 != 0)).sort((a, b) => a - b);
}



