const uniqueDigits = (x) => {
  return x.filter(v => !v.toString().includes('2') && !v.toString().includes('4') && !v.toString().includes('6') && !v.toString().includes('8'))
    .sort((a, b) => a - b);
}
