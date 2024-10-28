  return x.filter(num => !String(num).includes('2') && !String(num).includes('4') && !String(num).includes('6') && !String(num).includes('8') && !String(num).includes('0')).sort((a, b) => a - b);
}