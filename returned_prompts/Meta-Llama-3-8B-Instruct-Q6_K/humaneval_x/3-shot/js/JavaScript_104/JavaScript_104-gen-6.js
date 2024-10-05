  return x.filter(n => !String(n).includes('2')).sort((a, b) => a - b);
}